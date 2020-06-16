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
    abc = '{"id":"cb26d3bb-75c4-479c-aaec-0294825b7c2e","projectId":"fuse-ai","status":"QUEUED","source":{"storageSource":{"bucket":"59042334812.cloudbuild-source.googleusercontent.com","object":"fc22971857e5fb806ef41c283f3e6d824d2dcfd3-d8b9dace-0887-49cd-b2d7-6e4b6bb365e6.tar.gz"}},"steps":[{"name":"gcr.io/kaniko-project/executor:latest","args":["--destination=gcr.io/fuse-ai/built-with-kaniko-image1:fc22971857e5fb806ef41c283f3e6d824d2dcfd3","--cache=true"],"id":"Build1","timeout":"500s"},{"name":"gcr.io/kaniko-project/executor:latest","args":["--destination=gcr.io/fuse-ai/built-with-kaniko-image2:fc22971857e5fb806ef41c283f3e6d824d2dcfd3","--cache=true","--dockerfile=./flask/Dockerfile"],"id":"Build2","timeout":"500s"}],"createTime":"2020-06-16T08:44:32.890593788Z","timeout":"1000s","queueTtl":"3600s","logsBucket":"gs://codehub-cloudbuild-logs","sourceProvenance":{"resolvedStorageSource":{"bucket":"59042334812.cloudbuild-source.googleusercontent.com","object":"fc22971857e5fb806ef41c283f3e6d824d2dcfd3-d8b9dace-0887-49cd-b2d7-6e4b6bb365e6.tar.gz","generation":"1592297072635536"}},"buildTriggerId":"18baf66b-a911-476e-a0a1-ea66761f060c","options":{"substitutionOption":"ALLOW_LOOSE","dynamicSubstitutions":true,"logging":"LEGACY"},"logUrl":"https://console.cloud.google.com/cloud-build/builds/cb26d3bb-75c4-479c-aaec-0294825b7c2e?project=59042334812","substitutions":{"BRANCH_NAME":"stage","COMMIT_SHA":"fc22971857e5fb806ef41c283f3e6d824d2dcfd3","REPO_NAME":"onetrill","REVISION_ID":"fc22971857e5fb806ef41c283f3e6d824d2dcfd3","SHORT_SHA":"fc22971","_IMAGE1_NAME":"gcr.io/fuse-ai/built-with-kaniko-image1","_IMAGE1_VERSION":"v7.0.0","_IMAGE2_NAME":"gcr.io/fuse-ai/built-with-kaniko-image2","_IMAGE2_VERSION":"v8.0.0","_K8S_APP_NAME":"one-trill","_PROJECT_ID":"fuse-ai"},"tags":["fc22971857e5fb806ef41c283f3e6d824d2dcfd3","one-trill","trigger-18baf66b-a911-476e-a0a1-ea66761f060c"]}'
    cde = '{"id":"2ec9c474-1bc4-4dcf-9914-7062a65728bd","projectId":"fuse-ai","status":"SUCCESS","source":{"storageSource":{"bucket":"59042334812.cloudbuild-source.googleusercontent.com","object":"975ba242b541ca247499e7da18c58d94dafb0b3c-525e9fb6-7dfc-4b3c-9895-ace8410e80ad.tar.gz"}},"steps":[{"name":"gcr.io/kaniko-project/executor:latest","args":["--destination=gcr.io/fuse-ai/built-with-kaniko-image1:975ba242b541ca247499e7da18c58d94dafb0b3c","--cache=true"],"id":"Build1","timing":{"startTime":"2020-06-16T07:21:26.680377446Z","endTime":"2020-06-16T07:22:18.155907155Z"},"pullTiming":{"startTime":"2020-06-16T07:21:26.680377446Z","endTime":"2020-06-16T07:21:31.310418108Z"},"timeout":"500s","status":"SUCCESS"},{"name":"gcr.io/kaniko-project/executor:latest","args":["--destination=gcr.io/fuse-ai/built-with-kaniko-image2:975ba242b541ca247499e7da18c58d94dafb0b3c","--cache=true","--dockerfile=./flask/Dockerfile"],"id":"Build2","timing":{"startTime":"2020-06-16T07:22:18.155977622Z","endTime":"2020-06-16T07:23:03.195868632Z"},"pullTiming":{"startTime":"2020-06-16T07:22:18.155977622Z","endTime":"2020-06-16T07:22:18.157842007Z"},"timeout":"500s","status":"SUCCESS"}],"results":{"buildStepImages":["","sha256:8d8d7593f6da4e909bba63a3a22080eca935c57afd81ad0b8f069b90064324ba"],"buildStepOutputs":["",""]},"createTime":"2020-06-16T07:21:19.206209549Z","startTime":"2020-06-16T07:21:20.346583434Z","finishTime":"2020-06-16T07:23:04.041122Z","timeout":"1000s","queueTtl":"3600s","logsBucket":"gs://codehub-cloudbuild-logs","sourceProvenance":{"resolvedStorageSource":{"bucket":"59042334812.cloudbuild-source.googleusercontent.com","object":"975ba242b541ca247499e7da18c58d94dafb0b3c-525e9fb6-7dfc-4b3c-9895-ace8410e80ad.tar.gz","generation":"1592292078890716"},"fileHashes":{"gs://59042334812.cloudbuild-source.googleusercontent.com/975ba242b541ca247499e7da18c58d94dafb0b3c-525e9fb6-7dfc-4b3c-9895-ace8410e80ad.tar.gz#1592292078890716":{"fileHash":[{"type":"MD5","value":"jKLsTL+fW9+fpEtUNeZTZQ=="}]}}},"buildTriggerId":"18baf66b-a911-476e-a0a1-ea66761f060c","options":{"substitutionOption":"ALLOW_LOOSE","dynamicSubstitutions":true,"logging":"LEGACY"},"logUrl":"https://console.cloud.google.com/cloud-build/builds/2ec9c474-1bc4-4dcf-9914-7062a65728bd?project=59042334812","substitutions":{"BRANCH_NAME":"stage","COMMIT_SHA":"975ba242b541ca247499e7da18c58d94dafb0b3c","REPO_NAME":"onetrill","REVISION_ID":"975ba242b541ca247499e7da18c58d94dafb0b3c","SHORT_SHA":"975ba24","_IMAGE1_NAME":"gcr.io/fuse-ai/built-with-kaniko-image1","_IMAGE1_VERSION":"v7.0.0","_IMAGE2_NAME":"gcr.io/fuse-ai/built-with-kaniko-image2","_IMAGE2_VERSION":"v8.0.0","_K8S_APP_NAME":"one-trill","_PROJECT_ID":"fuse-ai"},"tags":["975ba242b541ca247499e7da18c58d94dafb0b3c","one-trill","trigger-18baf66b-a911-476e-a0a1-ea66761f060c"],"timing":{"BUILD":{"startTime":"2020-06-16T07:21:25.818677026Z","endTime":"2020-06-16T07:23:03.196063615Z"},"FETCHSOURCE":{"startTime":"2020-06-16T07:21:21.287270057Z","endTime":"2020-06-16T07:21:25.818623967Z"}}}'
    data = {'text': 'Hello world'}
    access_token = 'xoxb-1208014571248-1210301809888-2DMnaH6bSoMAW41jFbgtGGZu'
    headers={'Content-Type':'application/json'}
    auth = {'Authorization': 'Bearer xoxb-1208014571248-1210301809888-2DMnaH6bSoMAW41jFbgtGGZu'}
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(response)
if __name__=='__main__':
   hello_pubsub()
