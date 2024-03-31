#!/usr/bin/python3

# sourcery skip: use-fstring-for-formatting

"""script that fetches https://intranet.hbtn.io/status"""

import urllib.request


if __name__ == "__main__":
   
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print("Body response:")
            print("\t- type:", type(content))
            print("\t- content:", content)
            print("\t- utf8 content:", content.decode('utf-8'))
    except Exception as e:
        print("Error:", e)
