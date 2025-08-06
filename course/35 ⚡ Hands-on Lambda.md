# 35 ⚡ Hands-on Lambda

![](../imgs/4cc48aa363fb4fc483613ca8cb9f0f46.png)



## Instrument Lambda with Datadog

handler

```
datadog_lambda.handler.handler
```

Layer
runtime
```
arn:aws:lambda:us-east-1:464622532012:layer:Datadog-Python313:109
```

extension
```
arn:aws:lambda:us-east-1:464622532012:layer:Datadog-Extension:78
```

Add Tags:
* `DD_API_KEY`: `myapikey`
* `DD_LAMBDA_HANDLER`: `lambda_function.lambda_handler`
* `DD_SERVICE`: `simplelambda`
* `DD_SITE`: `datadoghq.com`
* `DD_TRACE_ENABLED`: `true`


