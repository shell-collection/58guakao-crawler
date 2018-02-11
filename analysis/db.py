import pymongo
from tutorial import settings


class MONGODB:

    def __init__(self):
        self.client = pymongo.MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT)
        self.db = self.client[settings.MONGO_DB]
        self.coll = self.db[settings.MONGO_COLL]

    def get_coll(self):
        return self.coll