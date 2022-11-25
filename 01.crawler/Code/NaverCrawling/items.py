# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NavercrawlingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title=scrapy.Field()
    content=scrapy.Field()
    date=scrapy.Field()
class NaverEdaily(scrapy.Item):
    title=scrapy.Field()
    content=scrapy.Field()
    date=scrapy.Field()