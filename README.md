# DestinyCollections
A list of all the collection items in Destiny 2, grabbed from the bungie.net API

## Setup
Create a file called ```config.json``` in the root directory and populate it like this:<br>
```
{
    "HEADERS": {
        "X-API-Key" : "<Bungie.net Api Key Here>"
    },
    "Account": {
        "membershipType": <Your Platform ID>,
        "destinyMembershipId": <Your Destiny Membership ID>
    }
}
```
## How to use
* Open Lookup.py
* Change the ```itemName``` variable to the name of the item you want to lookup
* Run the file
* Open up ```itemInfo.json``` to see the API info of the item

## How to recompile the JSON
* Change the ```if(True):``` to ```if(False):``` (This is here to prevent an accidental recompile)
* Run the ```compile.py``` file and leave it sit for a while<br>
This code isnt very efficient, as it iterates through items that have already been saved in the dictionary.

