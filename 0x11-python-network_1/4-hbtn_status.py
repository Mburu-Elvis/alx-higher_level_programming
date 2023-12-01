#!/usr/bin/python3
"""script fetching a url"""
import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = request.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
