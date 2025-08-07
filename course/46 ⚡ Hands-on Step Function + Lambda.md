# 46 ⚡ Hands-on Step Function + Lambda

![](../imgs/0d3825775ff14acfb83c59e244e99380.png)

https://docs.datadoghq.com/serverless/step_functions/merge-step-functions-lambda/?tab=serverlessframework

```
"Lambda Invoke": {
  "Type": "Task",
  "Resource": "arn:aws:states:::lambda:invoke",
  "Output": "{% $states.result.Payload %}",
  "Arguments": {
    "FunctionName": "MyFunctionName",

    "Payload": "{% ($execInput := $exists($states.context.Execution.Input.BatchInput) ? $states.context.Execution.Input.BatchInput : $states.context.Execution.Input; $hasDatadogTraceId := $exists($execInput._datadog.`x-datadog-trace-id`); $hasDatadogRootExecutionId := $exists($execInput._datadog.RootExecutionId); $ddTraceContext := $hasDatadogTraceId ? {'x-datadog-trace-id': $execInput._datadog.`x-datadog-trace-id`, 'x-datadog-tags': $execInput._datadog.`x-datadog-tags`} : {'RootExecutionId': $hasDatadogRootExecutionId ? $execInput._datadog.RootExecutionId : $states.context.Execution.Id}; $sfnContext := $merge([$states.context, {'Execution': $sift($states.context.Execution, function($v, $k) { $k != 'Input' })}]); $merge([$states.input, {'_datadog': $merge([$sfnContext, $ddTraceContext, {'serverless-version': 'v1'}])}])) %}"

  }
}
```

