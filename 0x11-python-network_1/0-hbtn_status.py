#!/usr/bin/python3
""" a script that fetches a URL"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'


def fetch_url():
    """function that fetches a URL"""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        headers = response.read().decode('utf-8')
    lines = headers.split('\n')
    print('Body response:')
    for key in lines:
        print(f'\t{key}')


if __name__ == '__main__':
    fetch_url()
