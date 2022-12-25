The Endpoint connection are usually ment to be used as a web socket connection, both for User Controller and Home Controller Devices.

GO Version : go1.20rc1 linux/amd64

# Build Docker Container

docker build -t 101bytes/autome-ai.service_controller .

# Create Container from Docker Image
docker run -it \
	-p 80:8000 -p 8001:8001 -p 8080:8080 -p 8081:8081 \
	-v /home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.SERVICE_CONTROLLER/app_data/bin:/usr/local/bin:ro \
	-v /home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.SERVICE_CONTROLLER/app_data/scripts:/scripts:ro \
	-v /home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.SERVICE_CONTROLLER/app_data/logs:/logs:rw \
	--name autome-ai.service_controller.id 101bytes/autome-ai.service_controller

OR

docker run -it \
        --expose=8000-8001 --expose=8080-8081 \
        -v /home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.SERVICE_CONTROLLER/app_data/bin:/usr/local/bin:ro \
        -v /home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.SERVICE_CONTROLLER/app_data/scripts:/scripts:ro \
        -v /home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.SERVICE_CONTROLLER/app_data/logs:/logs:rw \
        --name autome-ai.service_controller.id 101bytes/autome-ai.service_controller

# Start Docker container

docker start autome-ai.service_controller.id
