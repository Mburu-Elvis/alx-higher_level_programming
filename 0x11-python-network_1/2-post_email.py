#!/usr/bin/python3
"""script that posts an email"""
import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """function to send a post request to the url and email parameter."""
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
    print(f"Your email is: {email}")


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
