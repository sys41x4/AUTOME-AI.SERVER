
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import os
from datetime import datetime
from flask import Flask, redirect, url_for, request
import toml, json
import aiml

with open("SYSTEM.config", 'r') as f:
    SYSTEM_CONFIG_DATA = toml.loads(f.read())

with open("AI.config", 'r') as f:
    AI_CONFIG_DATA = toml.loads(f.read())

with open("HOME_CONTROLLER_COMMANDS.json", 'r') as f:
    HOME_CONTROLLER_COMMANDS = json.loads(f.read())

CURRENT_CONTROLLER_COMMAND = None
CURRENT_CONTROLLER_RESPONSE = None

NAME = AI_CONFIG_DATA["AI_CORE"]["NAME"]
GENDER = AI_CONFIG_DATA["AI_CORE"]["GENDER"]
BRAIN_LOAD_COMMAND = AI_CONFIG_DATA["AI_CORE"]["BRAIN_LOAD_COMMAND"]
BRAIN_FILEPATH = AI_CONFIG_DATA["AI_CORE"]["BRAIN_FILEPATH"]
BRAIN_BUILD_XML_FILEPATH = AI_CONFIG_DATA["AI_CORE"]["BRAIN_BUILD_XML_FILEPATH"]

# CURRENT_CONTROLLER_FETCHED_RESPONSE = ''

AIML_K = aiml.Kernel()

if os.path.exists(BRAIN_FILEPATH):
    AIML_K.loadBrain(BRAIN_FILEPATH)
    print("LOADED AI BRAIN: " + BRAIN_FILEPATH)

else:
    print("BUILDING AIML BRAIN FROM BRAIN MAP")
    AIML_K.bootstrap(learnFiles=BRAIN_BUILD_XML_FILEPATH, commands=BRAIN_LOAD_COMMAND)
    AIML_K.saveBrain(BRAIN_FILEPATH)
    print("CREATED AI BRAIN: " + BRAIN_FILEPATH)


command = ''
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'HOME PAGE'

# USER CONTROLLER ENDPOINTS #
@app.route('/ai/<data>')
def ai(data):
    # command = da
    if (home_controller(data)):
        response = "GETTING RESPONSE FROM THE ROOT HOME CONTROLLER"
        controller_response = "WAIT"
    else:
        response = AIML_K.respond(data)
        controller_response = None
    return {
    "RESPONSE": response,
    "CONTROLLER_RESPONSE": controller_response
    }

def chatbot(data):
    return AIML_K.respond(data)

def home_controller(data):
    '''
    '''
    global CURRENT_CONTROLLER_COMMAND
    if data.upper() in HOME_CONTROLLER_COMMANDS:
        CURRENT_CONTROLLER_COMMAND = HOME_CONTROLLER_COMMANDS[data.upper()]
        return True


@app.route('/fetch_home_controller_response')
def fetch_home_controller_response():
    global CURRENT_CONTROLLER_RESPONSE

    cmd = CURRENT_CONTROLLER_RESPONSE

    if cmd:
        CURRENT_CONTROLLER_RESPONSE=None
        status = 1
    else:
        status = 0


    return {"STATUS":status, "RESPONSE":cmd}


# HOME CONTROLLERS ENDPOINTS #
@app.route('/fetch_home_controller_command')
def fetch_home_controller_command():
    global CURRENT_CONTROLLER_COMMAND
    data_set = CURRENT_CONTROLLER_COMMAND
    CURRENT_CONTROLLER_COMMAND = None
    return {"DATA_SET":data_set}

@app.route('/push_home_controller_response/<data>')
def push_home_controller_command(data):
    global CURRENT_CONTROLLER_RESPONSE
    CURRENT_CONTROLLER_RESPONSE = data
    return {"STATUS": "SUCCESS", "TIMESTAMP":f"{datetime.now()}"}


# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host=SYSTEM_CONFIG_DATA["SERVICE_INFO"]["HOST"], port=SYSTEM_CONFIG_DATA["SERVICE_INFO"]["PORT"], debug=SYSTEM_CONFIG_DATA["SERVICE_INFO"]["DEBUG_MODE"])
