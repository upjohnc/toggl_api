import requests
import json
import pandas as pd


class Toggl(object):
    def __init__(self, username, password, workspace_id='2152928'):
        self.uname = username
        self.pwd = password
        self.workspace_id = workspace_id
        self.data_header = {'user_agent': 'upjohnc@gmail.com', 'workspace_id': self.workspace_id}
        self.url_ = 'https://toggl.com/reports/api/v2/details'

    def call_detail_report(self, start_date=None, end_date=None):
        if start_date is not None:
            self.data_header['since'] = start_date.strftime('%Y-%m-%d')
        if end_date is not None:
            self.data_header['until'] = end_date.strftime('%Y-%m-%d')
        response = requests.get(self.url_, auth=(self.uname, self.pwd), data=self.data_header).text
        json_acceptable_string = response.replace("'", "\"")
        data = json.loads(json_acceptable_string)
        return data

    @staticmethod
    def get_details_df(data):
        return pd.DataFrame(data['data'])
