#!/usr/bin/python3
"""
This Python script is a publisher
It publishes Markdown content on Medium.
"""
import json
import requests

USER_ID = 'tonybnya'
TOKEN = '220f05645f272eefa419154ec68a26cc8d18fe451d21718a140e6fc4c326fc5c3'
# URL = f'https://api.medium.com/v1/users/{USER_ID}/posts'
URL = f'https://api.medium.com/v1/publications/{USER_ID}/articles'

res = requests.get('https://medium.com')
XSRF = res.cookies.get('XSRF-TOKEN')

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-XSRF-TOKEN': XSRF,
}

with open('README.md', 'r') as file_obj:
    content = file_obj.read()

data = {
    'title': 'Postmortem',
    'contentFormat': 'markdown',
    'content': content,
    'publishStatus': 'draft',
}

response = requests.post(URL, headers=headers, data=json.dumps(data))

if response.status_code == 201:
    print('Article published successfully!')
else:
    print(f'Error: {response.text}')
