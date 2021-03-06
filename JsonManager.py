import json
import os

class JsonManager:
  def __init__(self, path):
    self.path = path
  def load(self):
    #opens json file and returns data
    with open(self.path, "r", encoding='utf-8') as theFile:
      return json.load(theFile) 

  def save(self, data):
    #opens json file and saves data
    with open(self.path, "w") as theFile:
      json.dump(data, theFile)
