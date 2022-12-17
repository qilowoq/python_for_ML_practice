import requests
from parameters import *
import json

def calc_salary(input_json):
    r = requests.post('http://' + HOST + ':' + str(PORT), json=input_json)
    return r.text

if __name__ == "__main__":
    input_json = json.load(open('input.json'))
    output_json = calc_salary(input_json)
    with open('output.json', 'w') as outfile:
        outfile.write(output_json)