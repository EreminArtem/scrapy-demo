# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class BooksPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.books

    def process_item(self, item, spider):
        title = item['title'].split(':')
        item['name'] = title[1][1:]
        item['author'] = title[0]
        del(item['title'])

        item['main_price'] = int(item['main_price'])
        item['special_price'] = int(item['special_price'])

        self.db[spider.name].insert_one(item)
        return item
