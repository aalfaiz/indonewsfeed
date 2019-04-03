import boto3

from scrapy.conf import settings
from boto3.dynamodb.types import TypeSerializer

class NewsRepository:
    def __init__(self):
        self.client = boto3.client('dynamodb')

    def save(self, item):

        
        response = self.client.put_item(
            TableName='article',
            Item = {
                'url' : {
                    'S' : item['url']
                },
                'title' : {
                    'S' : item['title']
                },
                'datetime' : {
                    'S' : item['datetime']
                },
                'source' : {
                    'S' : item['source']
                },
                'thumbnail_image_url' : {
                    'S' : item['thumbnail_image_url']
                },
                'thumbnail_image_alt' : {
                    'S' : item['thumbnail_image_alt']
                },
                'html_content' : {
                    'S' : item['html_content']
                },
                'text_content' : {
                    'S' : item['text_content']
                },
                 
            }
        )

    '''
    def is_link_exist(self, link):
        link = self.collection.find_one({"link":link})
        return link is not None and len(link) > 0
    '''
        