import os
import logging as logger
import requests
import json
from requests_oauthlib import OAuth1
from configs.hosts_config import API_HOSTS
# from src.utilities.credentialsUtility import CredentialsUtility

class RequestsUtility(object):

    def __init__(self):

        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        # wc_creds = CredentialsUtility.get_wc_api_keys()
        # self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])

    def post(self, endpoint, body_params=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        rs_api = requests.post(url=self.url, data=json.dumps(body_params), headers=headers, auth=None)
        self.status_code = rs_api.status_code
        # assert self.status_code == int(expected_status_code), f'Expected status code {expected_status_code} but actual is {self.status_code}'

        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()

        self.assert_status_code()
        logger.debug(f"POST API response: {rs_api.json()}")
        return self.rs_json

    def get(self, endpoint, body_params=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(body_params), headers=headers, auth=None)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"GET API response: {self.rs_json}")

        return self.rs_json

    def put(self, endpoint, body_params=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.put(url=self.url, data=json.dumps(body_params), headers=headers, auth=None)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"PUT API response: {self.rs_json}")

        return self.rs_json

    def delete(self, endpoint, body_params=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.delete(url=self.url, data=json.dumps(body_params), headers=headers, auth=None)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"DELETE API response: {self.rs_json}")

        return self.rs_json

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad Status code." \
          f"Expected {self.expected_status_code}, Actual status code: {self.status_code}," \
          f"URL: {self.url}, Response Json: {self.rs_json}"
