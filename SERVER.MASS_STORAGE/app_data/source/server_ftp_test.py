import os, sys
import toml
from pyftpdlib.authorizers import DummyAuthorizer as DA
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

SERVER_id = ''

base_config_filePath = "/usr/local/etc/AUTOME_AI/MASS_STORAGE/.config/.config"
serverType = "MASS_STORAGE"
ftps_key_filePath = "/usr/local/etc/AUTOME_AI/MASS_STORAGE/.keys/server_ftps_sample.key"
ftps_crt_filePath = "/usr/local/etc/AUTOME_AI/MASS_STORAGE/.cert/server_ftps_sample.crt"
speech_max_storage = 10240 # In MB | default allocation : 10GB | 1GB=1024MB
speech_storage_dir = "/assets/sound/speech_content"
ftps_expose_dir = "/assets"
ftps_host_ip = "0.0.0.0"
ftp_listner_port = 21

try:
    base_config_filePath = sys.argv[1]
except:
    pass

with open(base_config_filePath, 'r') as f:
    BASE_CONFIG_DATA = toml.loads(f.read())


def help():
    return f"""python3 {sys.argv[0]} <BASE_CONFIG_FILEPATH>
-h/--help : show this help info and exit
"""

try:
    with open(BASE_CONFIG_DATA["config_filePath"]["SERVER"], 'r') as f:
        SERVER_CONFIG_DATA = toml.loads(f.read())
except:
    print("SERVER CONFIG FILE UNAVAILABLE")
    print(help())
    sys.exit()

try:
    ftps_expose_dir = SERVER_CONFIG_DATA["FTPS_info"]["expose_dir"]
except:
    pass

try:
    ftps_host_ip = SERVER_CONFIG_DATA["FTPS_info"]["host"]
    ftp_listner_port = SERVER_CONFIG_DATA["FTPS_info"]["listner_port"]
except:
    pass

try:
    SERVER_id = SERVER_CONFIG_DATA["SERVER_info"]["ID"]
    speech_max_storage = SERVER_CONFIG_DATA["speech_storage_info"]["max_storage"]
    speech_storage_dir = SERVER_CONFIG_DATA["speech_storage_info"]["storage_dir"]
except:
    pass

ftps_key_filePath = SERVER_CONFIG_DATA["server_key_info"]["ftps_key_filePath"]
ftps_crt_filePath = SERVER_CONFIG_DATA["server_key_info"]["ftps_cert_filePath"]

# user and Permissions
try:
    with open(BASE_CONFIG_DATA["config_filePath"]["USER"], 'r') as f:USERS_ACCESS_CONFIG_DATA = json.load(f)

except:
    print("USERS List NOT FOUND")
    sys.exit()


print(f"""
SERVER ID : {SERVER_id}

STARTING FTPS SERVER AT
HOST : {ftps_host_ip}
PORT : {ftp_listner_port}
SPEECH STORAGE ALLOCATION : {speech_max_storage} MB
""")

# Reference : https://pyftpdlib.readthedocs.io/en/latest/api.html

def main():
    authorizer = DA()
    for USER_ACCESS_CONFIG_DATA in USERS_ACCESS_CONFIG_DATA.values():
        authorizer.add_user(USER_ACCESS_CONFIG_DATA['user'],USER_ACCESS_CONFIG_DATA['pass'],USER_ACCESS_CONFIG_DATA['dir'],perm=USER_ACCESS_CONFIG_DATA['perm'])
    # authorizer.add_anonymous("/app")
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "FTP | MASS_STORAGE"
    address=(ftps_host_ip,ftp_listner_port)
    server = FTPServer(address,handler)
    server.max_cons = 256
    server.max_cons_per_ip = 3
    server.serve_forever()

if __name__=='__main__':
    main()

