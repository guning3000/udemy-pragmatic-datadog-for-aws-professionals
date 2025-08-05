# 24 ⚡ Hands-on Log Tail

![](../imgs/cda28b5b8f6044fdbb667713dd629ff5.png)

https://docs.datadoghq.com/agent/logs/?tab=tailfiles

```yaml
logs:
  - type: file
    path: "<PATH_LOG_FILE>/<LOG_FILE_NAME>.log"
    service: "<APP_NAME>"
    source: "<SOURCE>"
```