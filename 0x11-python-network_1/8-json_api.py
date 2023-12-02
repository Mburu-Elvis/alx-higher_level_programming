#!/usr/bin/python3
"""script to send a POST request to the URL."""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    data = {'q': q}
    response = requests.post(url, data)
    try:
        res_json = response.json()
        if res_json:
            print(f'[{res_json[id]}] {res_json[name]}')
        else:
            print("No result")
    except:
        print("Not a valid JSON")
