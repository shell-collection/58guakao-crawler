# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from tutorial import settings


class TutorialPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT)
        self.db = self.client[settings.MONGO_DB]
        self.coll = self.db[settings.MONGO_COLL]

    def process_item(self, item, spider):
        post_item = dict(item)
        re = self.coll.find_one(post_item)
        if re is None:
            self.coll.insert(post_item)
            return "[%s] info save success!" % post_item['name']
        else:
            return "[%s] 已经存在!" % post_item['name']

