# 49 ⚡ Hands-on Datadog -> Log Archive -> Athena

![](../imgs/2f59d23a413f4e28925b8b1e684e0687.png)

https://docs.datadoghq.com/logs/log_configuration/forwarding_custom_destinations/?tab=http

```
CREATE EXTERNAL TABLE mytable (
  `date` STRING,
  host STRING,
  attributes MAP<STRING, STRING>,
  `_id` STRING,
  source STRING,
  message STRING,
  status STRING,
  tags ARRAY<STRING>
)
PARTITIONED BY (dt INT, hour INT)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3path'
```