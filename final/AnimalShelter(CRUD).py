import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import json

class AnimalShelter(object):
    def __init__(self, username, password):
        self.client = MongoClient('mongodb://%s:%s@localhost:35583/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']
            
            
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        
        
    # Create
    def create(self, data=dict()):
        if data is not None:
            self.database.animals.insert_one(data)
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    # Read       
    def read(self, data):
        if data is not None:
            return self.database.animals.find(data,{"_id":False})
        else:
            raise Exception("Nothing to find, because data parameter is empty")
        
    # Update        
    def update(self, find=dict(), replace=dict()):
        if find is not None:
            u = self.database.animals.update_many(find, {"$set" : replace})
            return json.dumps(str(u.modified_count) + 'updated records')
        else:
            raise Exception("Nothing to update, save is empty")
#     def update(self, save):
#          if save is not None:
#             if save:
#                  saveResult = self.database.animals.insert_one(save)
#             return saveResult;
#          else:
#             raise Exception("Nothing to update, save is empty")
            
    # Delete
    def delete(self, data=dict()):
        if data is not None:
            return json.dumps(self.database.animals.remove(data), indent = 4)
        else:
            return Exception("Nothing to delete, remove is empty")
        
#     def delete(self, remove):
#          if remove is not None:
#                 if removeResult:
#                     removeResult = self.database.animals.delete_one(remove)
#                     return removeResult;
#                 else:
#                     raise Exception("Nothing to delete, remove is empty")
