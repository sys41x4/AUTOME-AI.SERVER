The Endpoint connection are usually ment to be used as a web socket connection, both for User Controller and Home Controller Devices.
---

**GO Version** : go1.20rc1 linux/amd64

# Build Docker Container

`docker build -t 101bytes/autome-ai.dmz.web_socket_handler .`

# Create Container from Docker Image

```bash
docker run -d -it \
        --expose=80 --expose=8000-8001 --expose=8080-8081 \
        -v /.../SERVER.DMZ.WEB_SOCKET/app_data/bin:/usr/local/bin/AUTOME_AI/DMZ.WEB_SOCKET/bin:ro \
        -v /.../SERVER.DMZ.WEB_SOCKET/app_data/config:/usr/local/etc/AUTOME_AI/DMZ.WEB_SOCKET/.config:ro \
        -v /.../SERVER.DMZ.WEB_SOCKET/app_data/scripts:/scripts:ro \
        -v /.../SERVER.DMZ.WEB_SOCKET/app_data/info:/usr/local/etc/AUTOME_AI/DMZ.WEB_SOCKET/.info:ro \
        -v /.../SERVER.DMZ.WEB_SOCKET/app_data/dump:/usr/local/include/AUTOME_AI/DMZ.WEB_SOCKET/.dump:rw \
        -v /.../SERVER.DMZ.WEB_SOCKET/app_data/logs:/logs:rw \
        -v /.../SERVER.DMZ.WEB_SOCKET/app_data/assets:/assets:rw \
        --name autome-ai.dmz.web_socket_handler.id 101bytes/autome-ai.dmz.web_socket_handler
```

# Start Docker container

`docker start autome-ai.dmz.web_socket_handler.id`
