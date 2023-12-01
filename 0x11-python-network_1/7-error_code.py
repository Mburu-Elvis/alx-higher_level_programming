#!/usr/bin/python3
"""script that requests a URL and prints the error code on error"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    code = response.status_code
    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(response.text)
