import json
import pandas
import os

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")


dataset = pandas.DataFrame()

json_file_name = "json_files/erinata.json"

f = open(json_file_name, "r")
json_data = json.load(f)
f.close()



ghid = json_data['login']
gh_number_id = json_data['id']
name = json_data['name']

print(ghid)
print(gh_number_id)
print(name)