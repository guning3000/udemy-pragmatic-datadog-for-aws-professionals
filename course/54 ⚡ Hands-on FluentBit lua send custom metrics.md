# 54 ⚡ Hands-on FluentBit lua send custom metrics

![](../imgs/a024800f7da44ae7bd935ecc4c7ed2d5.png)

## setup fluent-bit container (for firelens)

conf
```

[INPUT]
    Name tcp
    Listen 127.0.0.1
    Port 8877
    Tag firelens-healthcheck

[INPUT]
    Name forward
    unix_path /var/run/fluent.sock

[INPUT]
    Name forward
    Listen 127.0.0.1
    Port 24224

[FILTER]
    Name                lua
    Match               *
    Script              script.lua
    call                run 

[OUTPUT]
    Name stdout
    Match **
```

script.lua
```lua
function run(tag, timestamp, record)

    package.path = './?.lua;/usr/local/share/luajit-2.1.0-beta3/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua;/usr/share/lua/5.1/?.lua;/usr/share/lua/5.1/?/init.lua;/usr/lib64/lua/5.1/?.lua;/usr/lib64/lua/5.1/?/init.lua'
    package.cpath = './?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so;/usr/lib64/lua/5.1/?.so;/usr/lib64/lua/5.1/loadall.so'

        local new_record = record

        if record["log"]:match("datadog") then
            local json = require('cjson')
            local https = require("ssl.https")

            local metrics_data = {
                series = {
                    {
                        metric = "mymetric",
                        type = 0,
                        points = {
                            {
                                timestamp = os.time(),
                                value = 0.7
                            }
                        },
                        tags = {
                            "env:dev",
                            "product:apple",
                        }
                    }
                }
            }


            local payload = json.encode(metrics_data)

            local url = "https://api.datadoghq.com/api/v2/series"
            local headers = {
                ["Content-Type"] = "application/json",
                ["Content-Length"] = #payload,
                ["DD-API-KEY"] = "myapikey" 
            }

            local response_body = {}

            local request_params = {
                url = url,
                method = "POST",
                headers = headers,
                source = ltn12.source.string(payload),
                sink = ltn12.sink.table(response_body)
            }

            local result, status_code, response_headers = https.request(request_params)
            new_record['dd_status_code'] = status_code

        end

        return 1, timestamp, new_record
end
```

epel.repo
```
[epel]
name=Extra Packages for Enterprise Linux 7 - $basearch
#baseurl=http://download.fedoraproject.org/pub/epel/7/$basearch
metalink=https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=$basearch
failovermethod=priority
enabled=1
gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

[epel-debuginfo]
name=Extra Packages for Enterprise Linux 7 - $basearch - Debug
#baseurl=http://download.fedoraproject.org/pub/epel/7/$basearch/debug
metalink=https://mirrors.fedoraproject.org/metalink?repo=epel-debug-7&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
gpgcheck=1

[epel-source]
name=Extra Packages for Enterprise Linux 7 - $basearch - Source
#baseurl=http://download.fedoraproject.org/pub/epel/7/SRPMS
metalink=https://mirrors.fedoraproject.org/metalink?repo=epel-source-7&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
gpgcheck=1
```

dockerfile
```dockerfile
FROM public.ecr.aws/aws-observability/aws-for-fluent-bit:latest

COPY ./epel.repo /etc/yum.repos.d/epel.repo

RUN yum -y install luarocks gcc gcc-c++ tar unzip lua-devel
RUN luarocks install luasocket 
RUN luarocks install luasec 
RUN luarocks install lua-cjson

COPY ./conf /conf
COPY ./script.lua /script.lua

CMD ["/fluent-bit/bin/fluent-bit", "-c" ,"/conf"]
```


```bash
export accid="654654299310"
export img="fluent-bit-lua-custom-metrics"
```

login
```bash
aws ecr get-login-password --region us-east-1 | docker login -u AWS --password-stdin $accid.dkr.ecr.us-east-1.amazonaws.com
```

create ecr
```
aws ecr create-repository --repository-name $img
```

build push
```bash
docker build -t $img .
docker tag $img $accid.dkr.ecr.us-east-1.amazonaws.com/$img:latest
docker push $accid.dkr.ecr.us-east-1.amazonaws.com/$img:latest
```

## app

```
public.ecr.aws/docker/library/python:3.12
```
