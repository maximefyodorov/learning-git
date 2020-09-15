import urllib.parse
import urllib.request
import json

url = 'https://hipsum.co/api/'
values = { 'type': 'hipster-centric', 'sentences': 5, 'start-with-lorem': 1 }

# data = urllib.parse.urlencode(values)
# url = '?'.join([url, data])
# response = urllib.request.urlopen(url)
# json_obj = json.loads(response.read())
# print(json_obj[0])

print(json.loads(urllib.request.urlopen('?'.join([url, urllib.parse.urlencode(values)])).read())[0])