# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LocalbankratesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LoanItem(scrapy.Item):
    type = scrapy.Field()
    age = scrapy.Field()
    term = scrapy.Field()
    rate = scrapy.Field()
    apr = scrapy.Field()
    
class DepositItem(scrapy.Item):
    institution_id = scrapy.Field()
    type = scrapy.Field()
    minBalance = scrapy.Field()
    interestRate = scrapy.Field()
    apr = scrapy.Field()