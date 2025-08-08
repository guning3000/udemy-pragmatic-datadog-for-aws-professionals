# 60 ⚡ Hands-on Sampling Logs using Edge Delta

![](../imgs/0de22e603c7549c0b3d0e6c16e508939.png)


https://docs.fluentbit.io/manual/2.0/pipeline/outputs/forward

```
docker run -it --rm public.ecr.aws/aws-observability/aws-for-fluent-bit:latest bash
```

```
[INPUT]
    Name    dummy
    Dummy   {"message":"info message", "level": "info"}
    Rate    100
    
[INPUT]
    Name    dummy
    Dummy   {"message":"err message", "level": "err"}
    Rate    100
    
[INPUT]
    Name    dummy
    Dummy   {"message":"warn message", "level": "warn", "service": "payments"}
    Rate    100
    
[OUTPUT]
    Name    stdout
    Match         *

[OUTPUT]
    Name          forward
    Match         *
    Host          127.0.0.1
    Port          24284
    Shared_Key    secret
    Self_Hostname flb.local
    tls           on
    tls.verify    off
```