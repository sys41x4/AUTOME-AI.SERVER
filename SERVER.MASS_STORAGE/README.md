# AUTOME-AI > SERVER > MASS_STORAGE
---

# BUILD Docker Image

docker build -t 101bytes/autome-ai.server.mass_storage .

# BUILD Containers from Docker Image

docker run -d -it \
        --expose=8000-8001 --expose=80-82 --expose=21 \
        -v /home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.MASS_STORAGE/app_data/bin:/usr/local/bin/AUTOME_AI/MASS_STORAGE/bin:ro \
        -v /home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.MASS_STORAGE/app_data/config:/usr/local/etc/AUTOME_AI/MASS_STORAGE/.config:ro \
        -v /home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.MASS_STORAGE/app_data/scripts:/scripts:ro \
        -v /home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.MASS_STORAGE/app_data/info:/usr/local/etc/AUTOME_AI/MASS_STORAGE/.info:ro \
        -v /home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.MASS_STORAGE/app_data/dump:/usr/local/include/AUTOME_AI/MASS_STORAGE/.dump:rw \
        -v /home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.MASS_STORAGE/app_data/assets:/assets:rw \
        --name autome-ai.server.mass_storage.id 101bytes/autome-ai.server.mass_storage

# Start Docker container

docker start autome-ai.server.mass_storage.id
