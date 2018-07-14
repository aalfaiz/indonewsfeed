# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from indonewsfeed.db_services import NewsRepository
from scrapy.exceptions import DropItem
from scrapy import log

class MongoDBPipeline(object):
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))

        repo = NewsRepository()
        if valid and not repo.is_link_exist(item["link"]):
            repo.save(item)
        return item
