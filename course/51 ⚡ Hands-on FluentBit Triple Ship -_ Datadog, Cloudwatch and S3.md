# 51 ⚡ Hands-on FluentBit Triple Ship -> Datadog, Cloudwatch and S3

![](../imgs/0b2cc08cd42e41e39d968e2fa6868346.png)


## fluentbit conf

https://github.com/aws/aws-for-fluent-bit/blob/mainline/use_cases/init-process-for-fluent-bit/README.md

fluentbit image
```
public.ecr.aws/aws-observability/aws-for-fluent-bit:init-latest
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

[OUTPUT]
    Name            s3
    Match           *
    bucket          yourbucket
    region          yourregion
    total_file_size 5120K  # 5MB in KB
    upload_timeout  10m
    store_dir       /var/log/flb_s3_buffer
    s3_key_format   /app_logs/%Y/%m/%d/%H_$UUID.log
    compression     gzip
    retry_limit     3
```


## app


`public.ecr.aws/docker/library/python:3.12`


