import os
import sys
import subprocess as sp
import json
import toml

base_config_filePath = ".config"

try:
    if sys.argv[1]:
        base_config_filePath = sys.argv[1]
except:
    pass

try:
    with open(base_config_filePath, "r") as f:base_config_data = toml.loads(f.read())

except:
    sys.exit()

with open(base_config_data["info_filePath"]["org"], "r") as f:org_info = toml.loads(f.read())

with open(base_config_data["config_filePath"]["image_build"], "r") as f:image_build_config_data = toml.loads(f.read())


docker_source = {
    "autome-ai.server.service_manager" : {"dirPath": "/home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.SERVICE_MANAGER", "count": 3},
    "autome-ai.server.internal.load_balancer": {"dirPath": "/home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.INTERNAL.LOAD_BALANCER", "count": 1},
    "autome-ai.server.external.load_balancer": {"dirPath": "/home/sys41x4/Desktop/AUTOME-AI/Server/SERVER.EXTERNAL.LOAD_BALANCER", "count":1}
}

container_info = {}

def build_images():
	# BUILD IMAGES

    for image in docker_source:
        print(f"IMAGE BUILDING | {org_info['org']['name']}/{image} | PROCESSING...")
        os.system(f"{image_build_config_data['virtualizer_info']['service_provider']} build -t {org_info['org']['name']}/{image} {docker_source[image]['dirPath']}")
        print(f"IMAGE BUILD | {org_info['org']['name']}/{image} | DONE :)")


def build_containers():

    for container in docker_source:
        # BUILD SERVER.service_manager
        if (container.endswith("server.service_manager")):
    	    for count_ in range(docker_source[container]['count']):
                print(f"CONTAINER BUILDING | {container}.{count_} | PROCESSING...")
                os.system(f"{image_build_config_data['virtualizer_info']['service_provider']} run -d -it --expose=8000-8001 --expose=8080-8081 -v {docker_source[container]['dirPath']}/app_data/bin:/usr/local/bin:ro -v {docker_source[container]['dirPath']}/app_data/scripts:/scripts:ro -v {docker_source[container]['dirPath']}/app_data/logs:/logs:rw --name {container}.{count_} {org_info['org']['name']}/{container}")
                print(f"CONTAINER BUILD | {container}.{count_} | DONE :)")

	# BUILD SERVER.EXTERNAL.LOAD_BALANCER
        elif (container.endswith("server.external.load_balancer")):
            for count_ in range(docker_source[container]['count']):
                print(f"CONTAINER BUILDING | {container}.{count_} | PROCESSING...")
                os.system(f"{image_build_config_data['virtualizer_info']['service_provider']} run -d -it --expose=80 --expose=8080-8082 --expose 5555 -v {docker_source[container]['dirPath']}/haproxy_config:/usr/local/etc/haproxy:rw --name {container}.{count_} {org_info['org']['name']}/{container}")
                print(f"CONTAINER BUILD | {container}.{count_} | DONE :)")

    print("*"*20)

def container_info_collect(dict_items):
    container_info.update(dict_items)

def container_get_ipAddr(container):

    ipv4 = sp.check_output((f"{image_build_config_data['virtualizer_info']['service_provider']}"+" inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "+f"{container}").split(" ")).strip().decode()[1:-1]

    container_info_collect({
f"{container}":{
 "ipv4": ipv4
 }
})

def dump_containers_info():
    with open(f"{base_config_data['dumps_Path']['dumps_dir']}/containers_info.{image_build_config_data['virtualizer_info']['service_provider']}.json", 'w') as f:
        json.dump(container_info_collect, f)

def start_containers():

    for container in docker_source:
        # BUILD SERVER.service_manager
        if (container.endswith("server.service_manager")):
            for count_ in range(docker_source[container]['count']):
                print(f"CONTAINER | STARTING | {container}.{count_} | PROCESSING...")

                os.system(f"{image_build_config_data['virtualizer_info']['service_provider']} start {container}.{count_}")
                os.system(f"{image_build_config_data['virtualizer_info']['service_provider']} exec -d -it {container}.{count_} /usr/local/bin/service_socket_handler 8080")

                print(f"CONTAINER | STARTED | {container}.{count_} | DONE :)")

                container_get_ipAddr(f"{container}.{count_}")

        # BUILD SERVER.EXTERNAL.LOAD_BALANCER
        elif (container.endswith("server.external.load_balancer")):
            for count_ in range(docker_source[container]['count']):
                print(f"CONTAINER | STARTING | {container}.{count_} | PROCESSING...")

                os.system(f"{image_build_config_data['virtualizer_info']['service_provider']} start {container}.{count_}")
                os.system(f"{image_build_config_data['virtualizer_info']['service_provider']} exec -d -it {container}.{count_} haproxy -f /usr/local/etc/haproxy/haproxy.cfg")

                print(f"CONTAINER | STARTED | {container}.{count_} | DONE :)")

                container_get_ipAddr(f"{container}.{count_}")
        print("*"*20)
    # dump_containers_info()
    print(json.dumps(container_info, indent=4))
    dump_containers_info()


def setup_SERVER_infrastructure():
    print("IMAGE BUILD INITIALIZED")
    build_images()
    print("IMAGE BUILD FINISHED")
    print("*"*30)

    print("CONTAINER BUILD INITIALIZED")
    build_containers()
    print("CONTAINER BUILD FINISHED")
    print("*"*30)

    print("CONTAINER START INITIALIZED")
    start_containers()
    print("CONTAINER STARTED")
    print("*"*30)


def main():
    while True:
        try:
            choice = input(f"""
Virtualizer : {image_build_config_data['virtualizer_info']['service_provider']}

[1] BUILD ALL IMAGES
[2] BUILD ALL CONTAINERS
[3] START ALL CONTAINERS
[4] STOP ALL CONTAINERS
[5] REMOVE ALL CONTAINERS
[6] REMOVE ALL IMAGES
[7] AUTO-SETUP SERVER INFRASTRUCTURE
[8] AUTO-REMOVE SERVER INFRASTRUCTURE
[9] EXIT

>>> """)

            if choice=="1": build_images()
            elif choice=="2": build_containers()
            elif choice=="3":start_containers()
            elif choice=="7":setup_SERVER_infrastructure()
            elif choice=="9":
                print("SEE YOU SOON :)")
                sys.exit()
        except KeyboardInterrupt:
            print("\nSEE YOU SOON :)")
            sys.exit()

if __name__=="__main__":
	main()
