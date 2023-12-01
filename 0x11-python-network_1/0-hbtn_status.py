#!/usr/bin/python3
""" a script that fetches a URL"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'


def fetch_url():
    """function that fetches a URL"""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        body = response.read()
    print('Body response:')
    print(f'\t- type: {type(body)}')
    print(f'\t- content: {body}')
    print(f'\t- utf8 content: {body.decode("utf-8")}')


if __name__ == '__main__':
    fetch_url()
