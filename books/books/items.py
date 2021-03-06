# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    main_price = scrapy.Field()
    special_price = scrapy.Field()
    rate = scrapy.Field()
