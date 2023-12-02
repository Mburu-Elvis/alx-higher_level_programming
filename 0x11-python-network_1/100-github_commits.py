#!/usr/bin/python3
"""10 most recent commits in rails holberton repository"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        counter = 0
        for commit in data:
            if counter ==  10:
                break
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f'{sha}: {author}')
            counter += 1
