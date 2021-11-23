#! /usr/bin/python3

import docker
import flask
from flask import request

def get_containers():
    container_list = client.containers.list()
    return (container_list)

def create_container(jsn):
    """
    Create container with given paramaters dict
    Returns True if succeful
    False if failed.
    """
    
    try:
        client.containers.run(jsn)
    except:
        return False
    return True

def create_network(jsn):
    pass

client = docker.from_env()
app = Flask(__name__)

@app.route('/api/run', methods=['POST'])
def run_container_post():
    return create_container(request.json)