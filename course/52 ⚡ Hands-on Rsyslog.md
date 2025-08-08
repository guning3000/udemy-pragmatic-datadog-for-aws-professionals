# 52 ⚡ Hands-on Rsyslog

![](../imgs/01a0fd2f6af741649179c41af3f32e95.png)

`yum -y install rsyslog`

https://www.datadoghq.com/architecture/using-rsyslog-to-send-logs-to-datadog/

```
logs:
  - type: tcp
    port: 10518
    service: "<APP_NAME>"
    source: "<CUSTOM_SOURCE>"
```