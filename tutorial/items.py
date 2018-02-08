# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    gender = scrapy.Field()
    name = scrapy.Field()
    age = scrapy.Field()
    life = scrapy.Field()
    education = scrapy.Field()
    address = scrapy.Field()
