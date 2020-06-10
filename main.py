import logging
from aiohttp import web
from aiohttp.web import Application, Request, Response
import asyncio
from aiohttp_sse import sse_response
import json

def chat(request):
    d = """
    <html>
      <head>
        <title>Tiny Chat</title>
        <script
        src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js">
        </script>
        <style>
        .messages {
          overflow: scroll;
          height: 200px;
        }
        .messages .sender{
          float: left;
          clear: left;
          width: 120px;
          margin-right: 10px;
          text-align: right;
          background-color: #ddd;
        }
        .messages .message{
          float: left;
        }
        form {
          display: inline;
        }
        </style>
        <script>
          $(function(){
            var source = new EventSource("/subscribe");
            source.addEventListener('message', function(event) {
              console.log(event.data)
              message = JSON.parse(event.data);
              $('.messages').append(
              "<div class=sender>"+message.sender+"</div>"+
              "<div class=message>"+message.message+"</div>");
            });
            $('form').submit(function(e){
              e.preventDefault();
              $.post('/everyone',
                {
                  sender: $('.name').text(),
                  message: $('form .message').val()
                })
              $('form .message').val('')
            });
            $('.change-name').click(function(){
              name = prompt("Enter your name:");
              $('.name').text(name);
            });
         });
        </script>
      </head>
      <body>
        <div class=messages></div>
        <button class=change-name>Change Name</button>
        <span class=name>Anonymous</span>
        <span>:</span>
      <form>
        <input class="message" placeholder="Message..."/>
        <input type="submit" value="Send" />
      </form>
      </body>
    </html>
    """
    resp = Response(text=d, content_type='text/html')

    return resp

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Welcome, " + name
    return Response(text=text)

async def message(request):
    app = request.app
    data = await request.post()
    print('data: ',data)
    for queue in app['channels']:
        payload = json.dumps(dict(data))
        await queue.put(payload)
    return Response()


async def subscribe(request):
    async with sse_response(request) as response:
        app = request.app
        queue = asyncio.Queue()
        print('Someone joined.')
        app['channels'].add(queue)
        try:
            while not response.task.done():
                payload = await queue.get()
                await response.send(payload)
                queue.task_done()
        finally:
            app['channels'].remove(queue)
            print('Someone left.')
    return response

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    app = Application(loop=loop)
    app['channels'] = set()
    app.router.add_route('GET', '/welcome', handle)
    app.router.add_route('GET', '/welcome/{name}', handle)
    app.router.add_route('GET', '/chat', chat)
    app.router.add_route('POST', '/everyone', message)
    app.router.add_route('GET', '/subscribe', subscribe)
    print("Hello world")
    web.run_app(app, host='127.0.0.1', port=9000)


