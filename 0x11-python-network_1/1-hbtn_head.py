#!/usr/bin/python3
"""script defining a function to send request to URL."""
import urllib.request
import sys


def request_id(url):
    """function to send a request to a URL and display a header value."""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        headers = response.info()
        id = headers.get('X-Request-Id')
        print(id)


if __name__ == '__main__':
    my_url = sys.argv[1]
    request_id(my_url)
