#To work with json file we have to import json module
import json
print("---------------------------------------------------------------------------------------------------------------\n")
#Python Read JSON File
# Open and read the JSON file using with
with open("sample1.json", 'r') as f:
    data = json.load(f)

# Print the data
print(data)
f.close()
print("---------------------------------------------------------------------------------------------------------------\n")

# Open and read the JSON file using file object
f1 = open("sample2.json", "r")
print(json.load(f1))
f.close()
print("---------------------------------------------------------------------------------------------------------------\n")

#Python Read JSON String and convert it into python object  (dictionary or list)
json_string1 = '{"name": "Shreyas", "Address": "Pune", "Age": 22}'

# deserializes into dict and returns dict.
f2 = json.loads(json_string1)

print("JSON string = ", f2)
print("---------------------------------------------------------------------------------------------------------------\n")

#Nested JSON String
json_string2 = '{"Student":{"name": "Shreyas", "Address": "Pune", "Age": 22}}'
f3 = json.loads(json_string2)
print("Nested JSON String = ", f3)
print(f3['Student']['name'])
print("---------------------------------------------------------------------------------------------------------------\n")

#Convert Python object into JSON string.
json_string1 = '{"name": "Shreyas", "Address": "Pune", "Age": 22}'
python_obj = {"Remark" : "Pass"}

print(json.dumps(python_obj))

#Update JSON String from python object
json_string= '{"name": "Shreyas", "Address": "Pune", "Age": 22}'
python_obj = {"Remark" : "Pass"}

json_new_string = json.loads(json_string)

json_new_string.update(python_obj)
print(json.dumps(json_new_string))

