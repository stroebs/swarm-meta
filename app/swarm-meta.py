#!/usr/bin/env python
import os
import docker
from flask import abort
from flask import Flask
from flask import request

docker_client = docker.from_env()
app = Flask(__name__)


def get_manager_token():
    try:
        token = str(docker_client.swarm.attrs['JoinTokens']['Manager'])
    except Exception as e:
        print('Error retrieving Manager Join Token: {}'.format(e))
        token = ''

    return token


def get_worker_token():
    try:
        token = str(docker_client.swarm.attrs['JoinTokens']['Worker'])
    except Exception as e:
        print('Error retrieving Worker Join Token: {}'.format(e))
        token = ''

    return token


@app.route('/token/manager/')
def return_manger_token():
    print('Source IP: {}'.format(request.remote_addr))

    return get_manager_token()


@app.route('/token/worker/')
def return_worker_token():
    print('Source IP: {}'.format(request.remote_addr))

    return get_worker_token()


if __name__ == '__main__':
    app.run(debug=False, port=8080, host='0.0.0.0')
