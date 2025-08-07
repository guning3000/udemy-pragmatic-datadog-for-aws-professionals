# 43 ⚡ Hands-on API Gateway Logs

![](../imgs/bce93871f3894cbb950a2469f71d1813.png)

https://docs.datadoghq.com/integrations/amazon-api-gateway/#log-collection

For the Log destination, make sure your CloudWatch **log group name starts with** `api-gateway`.

```json
{
    "apiId": "$context.apiId",
    "stage": "$context.stage",
    "requestId":"$context.requestId",
    "ip":"$context.identity.sourceIp",
    "caller":"$context.identity.caller",
    "user":"$context.identity.user",
    "requestTime":$context.requestTimeEpoch,
    "httpMethod":"$context.httpMethod",
    "resourcePath":"$context.resourcePath",
    "status":$context.status,
    "protocol":"$context.protocol",
    "responseLength":$context.responseLength
}
```
