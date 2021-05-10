from lxml import html
import requests
import json
import os

jsonmanager = __import__("JsonManager")

configjson = jsonmanager.JsonManager(os.path.realpath(os.path.join(os.path.dirname(__file__), "config.json")))
dictjson = jsonmanager.JsonManager(os.path.realpath(os.path.join(os.path.dirname(__file__), "dict.json")))
collections = jsonmanager.JsonManager(os.path.realpath(os.path.join(os.path.dirname(__file__), "collections.json")))

if(True):
    exit()

root_url = "https://www.bungie.net/Platform"
HEADERS = configjson.load()["HEADERS"]

collectibles = collections.load()['Response']['profileCollectibles']['data']['collectibles']

Dictionary = {}

counter = 0
for i in collectibles:
    counter += 1
    
    collectionItemHash = i
    
    url = f"/Destiny2/Manifest/DestinyCollectibleDefinition/{i}"
    res = requests.get(root_url+url, headers=HEADERS)
    
    itemName = json.loads(res.text)['Response']['displayProperties']['name']
    Dictionary[str(i)] = itemName
    
    if(not os.path.exists(f"C:\\Users\\Peter\\Documents\\code\\py\\Bungie net api\\dictionary\\hashes\\{i}.json")):
        theFile = open(f"C:\\Users\\Peter\\Documents\\code\\py\\Bungie net api\\dictionary\\hashes\\{i}.json", "x")
        json.dump(json.loads(res.text)["Response"], theFile)
        theFile.close()

    print(f"{counter} : {i}, {itemName}")

    if(counter % 100 == 0):
        dictjson.save(Dictionary)
    
        
dictjson.save(Dictionary)

