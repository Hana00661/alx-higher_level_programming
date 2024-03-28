#!/usr/bin/python3
"""
Module to access to the GitHub API and uses the information
"""
import sys
import requests


if __name__ == "__main__":
    try:
        repo_name = sys.argv[1]
        username = sys.argv[2]
        commmits_url = "https://api.github.com/repos/{}/{}/commits" \
            .format(username, repo_name)
        response = requests.get(commmits_url)
        json_obj = response.json()
        for i, obj in enumerate(json_obj):
            if i == 10:
                break
            if type(obj) is dict:
                name = obj.get('commit').get('author').get('name')
                print("{}: {}".format(obj.get('sha'), name))
    except ValueError as invalid_json:
        pass
