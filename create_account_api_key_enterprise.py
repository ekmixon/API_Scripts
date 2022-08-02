#!/usr/bin/env python
"""
Create an API key for your account
"""

import getpass
import requests
from urllib.parse import urljoin

username = input("Username: ")
password = getpass.getpass()

api_base_url = "https://api.probely.com"
auth_endpoint = urljoin(api_base_url, "enterprise/auth/obtain/")
keys_endpoint = urljoin(api_base_url, "keys/")

# Get login token
response = requests.post(auth_endpoint,
                         data={'username': username, 'password': password})
token = response.json()['token']

headers = {'Authorization': f"JWT {token}", 'Content-Type': "application/json"}

api_name = input("API key's name: ")

response = requests.post(
    keys_endpoint,
    headers=headers,
    json={'name': api_name})

if response.status_code == 201:
    print("\nAccount API key:", response.json()['key'])
    print("\nPlease record this key, it will not be shown again.")

else:
    print('\n[%s]\n%s' %(response.status_code, response.text))
