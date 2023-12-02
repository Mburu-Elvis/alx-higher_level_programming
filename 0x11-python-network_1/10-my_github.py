#!/usr/bin/python3
"""script that displays a gihub's user id"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(user, password)
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        data = response.json()
        print(data.get('id'))
    else:
        print(None)
