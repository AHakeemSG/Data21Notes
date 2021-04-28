# Working with JSON

import json

# 1st activity - pet data
pet_data = {"name": "Bob", "food": "carrots"}

# print(type(pet_data))
#
# pet_data_json_str = json.dumps(pet_data)  # .dumps transforms dict into serialised string
# print(pet_data_json_str)
# print(type(pet_data_json_str))

# # .dump - creates a streamed object/file  - whereas .dumps sealrises the object
# with open("new_json_file.json", "w") as jsonfile:
#     json.dump(pet_data, jsonfile)

with open("new_json_file.json") as jsonfile:
    pet = json.load(jsonfile)  # grabs the json file and loads it into a python dictionary
    print(type(pet))
    print(pet["name"])  # type is now a dictionary therefore we can treat it as such



# 2nd activity - exhange rates

# Grabbing the json file - exchange rates.json
class RatesParser:

    def __init__(self, rates_file):
        rates_info = self._open_json_file(rates_file)
        self.base = rates_info["base"]
        self.rates = rates_info["rates"]
        self.gbp = self.rates["GBP"]
    #   self.gbp = rates_info["rates"]["GBP"]  # double index to just retreive GBP

    def _open_json_file(self, file):
        with open(file) as rates:
            return json.load(rates)


# reading the file
rates_reader = RatesParser("exchange_rates.json")
print(rates_reader.gbp)
