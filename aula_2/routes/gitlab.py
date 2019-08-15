import sys
import os
import time

import flask
import requests

blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET', 'POST' ])
def gitlab():
    headers = {
        'Private-Token': 'pQyP9oUuy-wsEwj1VJWf'
    }
    res_1 = requests.get('http://localhost:8000/api/v4/users', headers=headers)
    users = res_1.json() if res_1.status_code == 200 else []

    res_2 = requests.get('http://localhost:8000/api/v4/projects', headers=headers)
    projects = res_2.json() if res_2.status_code == 200 else []

    print("Test---->" + str(projects))
    #Teste doido
    context = {
        'title': 'Python | Sysadmin',
        'users': users,
        'projects': projects

    }
    return flask.render_template('gitlab.html', context=context)


