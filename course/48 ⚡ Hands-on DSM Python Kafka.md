# 48 ⚡ Hands-on DSM Python Kafka

![](../imgs/e4f4319cc4ac4ca8b8af9d398e3962bf.png)

https://docs.datadoghq.com/data_streams/

## 3 EC2 instances

## start kafka container

```bash
docker run -dit --name kafka \
  -p 9092:9092 \
  -e KAFKA_ENABLE_KRAFT=yes \
  -e KAFKA_CFG_PROCESS_ROLES=broker,controller \
  -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER \
  -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 \
  -e KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT \
  -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092 \
  -e KAFKA_CFG_BROKER_ID=1 \
  -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@kafka:9093 \
  -e ALLOW_PLAINTEXT_LISTENER=yes \
  -e KAFKA_KRAFT_CLUSTER_ID=r4zt_wrqTRuT7W2NJsB_GA \
  bitnami/kafka:3.3.1 
```

## producer app

deps
```bash
pip3 install ddtrace requests confluent-kafka
```

envs
```
export DD_DATA_STREAMS_ENABLED=true
export DD_ENV=dev
export DD_SERVICE=kafka-producer-app
```

```python
import random
import sys
import time
from ddtrace import tracer
import requests
from confluent_kafka import Producer
import os

host = ""

p = Producer({'bootstrap.servers': f'{host}:9092'})

while True:
    topic = f"mytopic"

    p.produce(topic, "asdfasdf".encode('utf-8'))
    print("ok")
    p.flush()
    print("flush")
    time.sleep(1)
```


## consumer app

envs
```
export DD_DATA_STREAMS_ENABLED=true
export DD_ENV=dev
export DD_SERVICE=kafka-consumer-app
```

```python
import random
import sys
import time
from ddtrace import tracer
import requests
from confluent_kafka import Consumer
import os

host = ""

topic = f"mytopic"

c = Consumer({
    'bootstrap.servers': f'{host}:9092',
    'group.id': f'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe([topic])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()
```


