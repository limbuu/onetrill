import base64
import requests
import json
def hello_pubsub():
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    #pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    #print(pubsub_message)

    url = 'https://hooks.slack.com/services/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'
    data = {'text': 'gdhchschschbshcbshbchscbscscscsdcs'}
    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)
if __name__=='__main__':
   hello_pubsub()

