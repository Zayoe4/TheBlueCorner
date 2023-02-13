import json
import os
script_dir = os.path.dirname(__file__)
print(script_dir)
rel_path = "//config.json"
abs_file_path = os.path.join(script_dir, rel_path).replace('\\', '/')

accountsList = []
myFile = open("accounts.txt")

accounts = myFile.readlines()

for account in accounts:
    username = account.strip().split(":")[0]
    password = account.strip().split(":")[1]
    accountDict = {"username":username,"password":password}
    accountsList.append(accountDict)
accountDict = {"accounts":accountsList,"target_configuration_url":'C:\\Users\\ruadd\\Desktop\\placebot-main\\out.cfg'}
print(abs_file_path)
myFile.close()
with open(abs_file_path,'w') as jsonFile:
    json.dump(accountDict, jsonFile, indent=2)

