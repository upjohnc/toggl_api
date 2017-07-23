from toggl_api import api
import yaml


def get_data():
    with open('config.yaml') as file:
        config = yaml.load(file)

    credentials = config['credentials']

    t = api.Toggl(credentials['uname'], credentials['pwd'])

    t.call()
    return t.data
