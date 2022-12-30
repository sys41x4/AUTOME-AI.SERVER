1. Currently initializing "CMD /scripts/init.sh" in **Dockerfile** leads to crash of the container after image creation
   so the "dmz.ws" binary located at "/usr/bin/AUTOME_AI/DMZ.WEB_SOCKET/bin/dmz.ws", should manually be triggered after starting of the container created from the docker image,
   to initialize websocket connection through the docker container

   
