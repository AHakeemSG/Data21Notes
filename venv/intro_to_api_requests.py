import requests
import json
from pprint import pprint

# Get request
post_code_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

# print(post_code_req.json())  # retrieves data of the content for the postcode that was indicated


# Post request
# create a list of post codes
json_body = json.dumps({"postcodes": ["PR3 0SG", "PR3 0SG", "EX165BL", "BN3 7GX"]})  # searlising the object into a json string

headers = {"Content-Type": "application/json"}  # tells the server that we are expecting a content type i.e. a json

# posting multiple requests
post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_body)

# We can use pprint to format the dictionary so the content is more human readable
pprint(post_multi_req.json())


# Paula's step by step guide for getting requests
