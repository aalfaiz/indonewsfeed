import pymongo

from scrapy.conf import settings

class NewsRepository:
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )

        database = connection[settings['MONGODB_DB']]
        self.collection = database[settings['MONGODB_COLLECTION']]

    def save(self, item):
        self.collection.insert(dict(item))

    # def is_exist(self, link):
        
