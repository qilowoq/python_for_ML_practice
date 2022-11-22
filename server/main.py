import requests
from parameters import *


r = requests.post('http://' + HOST + ':' + str(PORT), json={"year": 2022, "month": 10, "salary": 120000})
print(r.text)