import pymongo
from tutorial import settings
from tutorial.items import TutorialItem


class Test:
    def __init__(self):
        self.client = pymongo.MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT)
        self.db = self.client[settings.MONGO_DB]
        self.coll = self.db[settings.MONGO_COLL]

    def test(self):
        item = TutorialItem()
        item['name'] = '侯飞'
        post_item = dict(item)
        result = self.coll.find_one(post_item)
        print(result)


if __name__ == '__main__':
    test = Test()
    test.test()