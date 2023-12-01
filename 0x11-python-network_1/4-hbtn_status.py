#!/usr/bin/python3
"""script fetching a url"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    print("Body response:")
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body.decode('utf-8')}")
