#!/usr/bin/python3
"""script that takes URL from user input and sends request."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    headers = response.headers
    print(headers.get('X-Request-Id'))
