# 14 ⚡ Hands-on Frontend -> Lambda -> DynamoDB

![](../imgs/4a64ec6dae78401fb0a5e0e586bd9df6.png)

## Frontend code

```html
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    * {
      font-size: 40px;
    }
  </style>
</head>
<body>
  <h3>POST</h3> 
  <b>key</b>: <input type="text" style="font-size:30px;" id="postkey"/><br>
  <b>message</b>: <input type="text" style="font-size:30px;" id="postmsg"/><br>
  <button id="postbutton">POST</button> 
  <br>
  <textarea id="postrs" style="width:600px;height:300px;"></textarea>
  <br>
  <h3>GET</h3> 
  <b>key</b>: <input type="text" style="font-size:30px;" id="getkey"/>
  <button id="getbutton">GET</button>
  <br>
  result:<br>
  <textarea id="getrs" style="width:600px;height:300px;"></textarea>
  <script>
    var postkey = document.querySelector('#postkey')
    var postmsg = document.querySelector('#postmsg')
    var postbutton = document.querySelector('#postbutton')
    var postrs = document.querySelector('#postrs')
    var getbutton = document.querySelector('#getbutton')
    var getkey = document.querySelector('#getkey')
    var gertrs = document.querySelector('#getrs')

    var url = 'myurl'

    postbutton.addEventListener('click', () => {
      fetch(url, {
        method: 'POST',
        body: JSON.stringify({
          key: postkey.value,
          msg: postmsg.value,
        })
      }).then(rs => rs.json())
      .then(rs => {
        postrs.value = JSON.stringify(rs, null, 4)
      })
    })
    getbutton.addEventListener('click', () => {
      fetch(url+getkey.value).then(rs => rs.json())
      .then(rs => {
        getrs.value = JSON.stringify(rs, null, 4)
      })
    })
  </script>
</body>
</html>
```

## Lambda code

```python
import json
import boto3

def lambda_handler(event, context):
    ddb = boto3.client('dynamodb')
    tablename = 'mytb'
    if event['requestContext']['http']['method'] == 'POST':
        data = json.loads(event['body'])
        rs = ddb.put_item(
            TableName=tablename,
            Item={
                "key": {"S": data['key']},
                "msg": {"S": data['msg']},
            }
        )
        return json.dumps(rs)
    else:
        key = event['requestContext']['http']['path'][1:]
        rs = ddb.get_item(
            TableName=tablename,
            Key={"key": {"S": key}}
        )
        return json.dumps(rs['Item'])
```
