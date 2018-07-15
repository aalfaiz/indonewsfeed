import pymongo

from scrapy.conf import settings

class NewsRepository:
    def __init__(self):
        
        uri = settings['MONGODB_URI']
        connection = pymongo.MongoClient(uri)

        database = connection[settings['MONGODB_DB']]
        self.collection = database[settings['MONGODB_COLLECTION']]

    def save(self, item):
        self.collection.insert(dict(item))

    def is_link_exist(self, link):
        link = self.collection.find_one({"link":link})
        return link is not None and len(link) > 0
        