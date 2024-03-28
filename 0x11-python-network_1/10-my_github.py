#!/usr/bin/python3
"""script that takes your GitHub credentials
(username and password) and uses the GitHub
API to display your id"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(argv[1], argv[2]))
    myobj = response.json()
    try:
        print(myobj["id"])
    except KeyError:
        print("None")
