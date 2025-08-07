# 50 ⚡ Hands-on FluentBit Dual Ship -> Datadog and Cloudwatch

![](../imgs/e8c579413291443c8747af81c1ed6f2e.png)

## fluentbit conf

fluentbit image
```
public.ecr.aws/aws-observability/aws-for-fluent-bit:stable
```

https://github.com/aws-samples/amazon-ecs-firelens-examples/blob/mainline/examples/fluent-bit/multi-config-support/task-definition.json

```
"environment": [
        {
            "name": "aws_fluent_bit_init_s3_1",
            "value": "arn:aws:s3:::your-bucket/tail-input.conf"
        },
```

```
# CloudWatch Output
[OUTPUT]
    Name                cloudwatch
    Match               *
    region              us-east-1
    log_group_name      /fluent-bit/dummy-logs
    log_stream_name     host
    auto_create_group   true

# Datadog Output
[OUTPUT]
    Name                datadog
    Match               *
    Host                http-intake.logs.datadoghq.com
    TLS                 on
    apikey              ${DD_API_KEY} 
    dd_service          fluent-bit-example
    dd_source           dummy
    dd_tags             env:production
```


## app


## simple flask application

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
export img="myflaskfluentbitdualship"
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

