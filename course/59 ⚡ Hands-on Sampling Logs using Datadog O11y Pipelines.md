# 59 ⚡ Hands-on Sampling Logs using Datadog O11y Pipelines

![](../imgs/019e10bcbbc44359906fd63b3e765f0b.png)

https://www.datadoghq.com/blog/observability-pipelines-log-volume-control/?_gl=1*q0tx3*_gcl_au*NTc2NTk2MTUuMTc0Njk4MjI5MC4yOTUyMzQ3MTIuMTc1NDE5MzM2Ny4xNzU0MTkzMzkw*_ga*NTM5Mzg5MzYwLjE3NDg3MDY0NzU.*_ga_KN80RDFSQK*czE3NTQ2Mjc1NzckbzE0JGcwJHQxNzU0NjI3NjM3JGo2MCRsMCRoMTAwNjY2NzQzNw..*_fplc*ZGxnTCUyRkFSd1dUUCUyRnhDU1FJV1g0ak0lMkZsJTJGclBDRjRUUW05NUIlMkIyN29yRDJuRzNUSk5LbURRNHFUSzVJZkszUzZQakNaamslMkIzU1liYU1TWjNlZUdRdlFUWldUSlhuWEUyUTRiaDNxNUZUQnFyeFhhSDByY1RhVXklMkZtb25WTFElM0QlM0Q.

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