#!/usr/bin/python3
"""this takes your GitHub credentials (username and password) and uses
-the GitHub API to display your id
-use Basic Authentication with a personal access token as password to
-access to your information (only read:user permission is needed)
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
