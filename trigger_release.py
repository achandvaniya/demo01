import requests
import json
import os

session = requests.Session()


session.auth = (os.environ['username'], os.environ['token'])

url = "https://dev.azure.com/ajaycs1991/ajaycs1991/_apis/pipelines/1/runs?api-version=7.1-preview.1"

auth = session.post(url)

payload = json.dumps({
  "templateParameters": {
    "name": "ac"
  }
})

headers = {
  'Content-Type': 'application/json',
}

response = session.post(url, headers=headers, data=payload)

print(response.text)