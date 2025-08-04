# 12 ⚡ Hands-on Angular application

![](../imgs/18a89e0680cc40a3824c241360107047.png)


```bash
npm i -g @angular/cli
```

```bash
ng new angular-app --no-strict
```

start sample app
```bash
npm run start -- --host 0.0.0.0 
```

https://docs.datadoghq.com/real_user_monitoring/browser/setup/client?tab=rum#cdn-async
```js
<script>
  (function(h,o,u,n,d) {
     h=h[d]=h[d]||{q:[],onReady:function(c){h.q.push(c)}}
     d=o.createElement(u);d.async=1;d.src=n
     n=o.getElementsByTagName(u)[0];n.parentNode.insertBefore(d,n)
  })(window,document,'script','https://www.datadoghq-browser-agent.com/us1/v6/datadog-rum.js','DD_RUM')
  window.DD_RUM.onReady(function() {
    window.DD_RUM.init({
      clientToken: '<CLIENT_TOKEN>',
      applicationId: '<APPLICATION_ID>',
      // `site` refers to the Datadog site parameter of your organization
      // see https://docs.datadoghq.com/getting_started/site/
      site: 'datadoghq.com',
      //  service: 'my-web-application',
      //  env: 'production',
      //  version: '1.0.0',
      sessionSampleRate: 100,
      sessionReplaySampleRate: 100,
      enablePrivacyForActionName: true,
    });
  })
</script>
```

extra content

https://docs.datadoghq.com/tracing/other_telemetry/rum/?tab=browserrum

```js
window.DD_RUM.init({
   clientToken: '<CLIENT_TOKEN>',
   applicationId: '<APPLICATION_ID>',
   site: 'datadoghq.com',
   //  service: 'my-web-application',
   //  env: 'production',
   //  version: '1.0.0',
   allowedTracingUrls: ["https://api.example.com", /https:\/\/.*\.my-api-domain\.com/, (url) => url.startsWith("https://api.example.com")],
   sessionSampleRate: 100,
   sessionReplaySampleRate: 100, // if not included, the default is 100
   trackResources: true,
   trackLongTasks: true,
   trackUserInteractions: true,
 })
```


