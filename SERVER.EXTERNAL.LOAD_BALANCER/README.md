# AUTOME-AI LOAD BALENCER
---

Technology Used :

1. HAProxy
2. DOCKER ALPINE




CREATE DOCKER IMAGE FROM APP
`docker build -t 101bytes/autome-ai.load_balancer .`


Assuming the `Dockerfile` file is present in the current location

`docker run -d --name autome-ai.load_balancer --expose 5555 -v /path/to/etc/haproxy_config:/usr/local/etc/haproxy:rw 101bytes/autome-ai.load_balancer`

OR

`docker run -it -p 8000:80 --expose 5555 -v /home/sys41x4/Desktop/AUTOME-AI/Server/LOAD_BALENCER/AUTOME-AI_LOAD_BALENCER/haproxy_config:/usr/local/etc/haproxy:rw --name autome-ai.load_balancer 101bytes/autome-ai.load_balancer`

BUILD DOCKER CONTAINER FROM IMAGE
`docker run -it -p 8000:80 --name autome-ai.load_balancer 101bytes/autome-ai.load_balancer`

START DOCKER CONTAINER
`docker start autome-ai.load_balancer`

EXECUTE COMMAND IN CONTAINER BACKGROUND AFTER STARTING CONTAINER
`docker exec -d autome-ai.load_balancer haproxy -f /usr/local/etc/haproxy/haproxy.cfg`

---

CHECK `my-running-haproxy` container status
`docker ps`
