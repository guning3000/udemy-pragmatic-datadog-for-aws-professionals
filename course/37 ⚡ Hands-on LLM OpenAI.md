# 37 ⚡ Hands-on LLM OpenAI

![](../imgs/659472717ad1441d95fd1a624b51f219.png)

https://docs.datadoghq.com/llm_observability/instrumentation/sdk/?tab=python

## app code

```python
import os
from openai import OpenAI
import ddtrace
ddtrace.patch_all()
from ddtrace.llmobs import LLMObs
LLMObs.enable(
  ml_app="myopenapiapp",
  api_key=os.environ['DD_API_KEY'],
  site="datadoghq.com",
  agentless_enabled=True,
)

def lambda_handler(event,context):
    oai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    completion = oai_client.chat.completions.create(
     model="gpt-3.5-turbo",
     messages=[
      {"role": "system", "content": "You are a helpful customer assistant for a furniture store."},
      {"role": "user", "content": "I'd like to buy a chair for my living room."},
    ],
    )

    print(completion)
    LLMObs.flush()
    return {
            "statusCode": 200
    }
```

## dockerfile

```dockerfile
FROM public.ecr.aws/lambda/python:3.11

RUN pip3 install openai ddtrace

ENV DD_API_KEY=
ENV OPENAI_API_KEY=
ENV DD_LLMOBS_ENABLED=1
ENV DD_LLMOBS_ML_APP=myopenaiapp
ENV DD_SERVICE=myopenaiapp
ENV DD_LLMOBS_AGENTLESS_ENABLED=1
ENV DD_TRACE_ENABLED=true
ENV DD_SITE=datadoghq.com

COPY ./app.py /var/task/app.py

CMD ["app.lambda_handler"]
```


```bash
export accid="654654299310"
export img=myopenai
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

