#!/usr/bin/python3
"""script that sends a POST request to a URL."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    try:
        response = requests.post(url, data)
        print(response.text)
    except Exception as e:
        print("Error: {}".format(e))
