# 33 ⚡ Hands-on Auto Instrumentation Flask

![](../imgs/40884acbed2e4cfd8c4b80bb04680391.png)

## Setup admission controller

```yaml
clusterAgent:
  #(...)
  ## @param admissionController - object - required
  ## Enable the admissionController to automatically inject APM and
  ## DogStatsD config and standard tags (env, service, version) into
  ## your pods
  #
  admissionController:
    enabled: true
```

## upgrade helm

`helm upgrade datadog-agent -f datadog-values.yaml datadog/datadog`

## create flask app image ECR

```python
from flask import Flask
import logging

# Basic configuration
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def hello_world():
    logging.info("request received") 
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

dockerfile

```
FROM public.ecr.aws/docker/library/python:3.12

COPY ./app.py /app.py

RUN pip3 install flask flask-cors

CMD ["python3", "/app.py"]
```

```bash
export accid="654654299310"
export img="flaskadmission"
```

login
```bash
aws ecr get-login-password --region us-east-1 | docker login -u AWS --password-stdin $accid.dkr.ecr.us-east-1.amazonaws.com
```

create ecr
```
aws ecr create-repository --repository-name $img
```

build push
```bash
docker build -t $img .
docker tag $img $accid.dkr.ecr.us-east-1.amazonaws.com/$img:latest
docker push $accid.dkr.ecr.us-east-1.amazonaws.com/$img:latest
```

## run pod with admission control

https://docs.datadoghq.com/containers/troubleshooting/admission-controller/?tab=helm

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: example-deployment
spec:
  #(...)  
  template:
    metadata:
      labels:
        admission.datadoghq.com/enabled: "true"
      annotations:
        admission.datadoghq.com/<LANGUAGE>-lib.version: <VERSION>
    spec:
      containers:
      #(...)
```

https://docs.datadoghq.com/tracing/guide/local_sdk_injection/#step-2-annotate-pods-for-library-injection

`admission.datadoghq.com/python-lib.version: "<CONTAINER IMAGE TAG>"`

versions
https://github.com/DataDog/dd-trace-py/releases
python 3.11.2


## caveat

https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/kubernetes/?tab=agentv764recommended#enable-apm-on-your-applications

Single Step Instrumentation does not instrument applications in the namespace where the Datadog Agent is installed. Install the Agent in a separate namespace where you do not run your applications.






