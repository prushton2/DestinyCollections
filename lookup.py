import os


jsm = __import__("JsonManager")
dictionary = jsm.JsonManager(os.path.realpath(os.path.join(os.path.dirname(__file__), "dict.json")))
output = jsm.JsonManager(os.path.realpath(os.path.join(os.path.dirname(__file__), "itemInfo.json")))

def lookup(json_object, name):
    for i in json_object:
        if json_object[i] == name:
            return i

#    HERE    #
itemName = "No Love Lost"


id = lookup(dictionary.load(), itemName)
print(f'{itemName}: {id}')

hashes = jsm.JsonManager(os.path.realpath(os.path.join(os.path.dirname(__file__), f"hashes\\{id}.json")))

output.save(hashes.load())
print(f"saved")