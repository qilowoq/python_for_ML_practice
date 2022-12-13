import requests
from parameters import *
import json

input_json = json.load(open('input.json'))

r = requests.post('http://' + HOST + ':' + str(PORT), json=input_json)

with open('output.json', 'w') as outfile:
    outfile.write(r.text)