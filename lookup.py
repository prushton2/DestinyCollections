jsm = __import__("JsonManager")
dictionary = jsm.JsonManager("C:\\Users\\Peter\\Documents\\code\\py\\Bungie net api\\dictionary\\dict.json")
output = jsm.JsonManager("C:\\Users\\Peter\\Documents\\code\\py\\Bungie net api\\dictionary\\itemInfo.json")

def lookup(json_object, name):
    for i in json_object:
        if json_object[i] == name:
            return i

itemName = "No Love Lost"


id = lookup(dictionary.load(), itemName)
print(f'{itemName}: {id}')

hashes = jsm.JsonManager(f"C:\\Users\\Peter\\Documents\\code\\py\\Bungie net api\\dictionary\\hashes\\{id}.json")

output.save(hashes.load())
print(f"saved")