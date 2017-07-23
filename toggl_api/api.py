import requests


class Toggl(object):
    def __init__(self, username, password, workspace_id='2152928'):
        self.uname = username
        self.pwd = password
        self.workspace_id = workspace_id
        self.data_header = {'user_agent': 'upjohnc@gmail.com', 'workspace_id': self.workspace_id}
        self.url_ = 'https://toggl.com/reports/api/v2/details'
        self.data = None

    def call(self):
        self.data = requests.get(self.url_, auth=(self.uname, self.pwd), data=self.data_header).text
