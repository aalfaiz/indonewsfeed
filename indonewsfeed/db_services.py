import boto3

from scrapy.conf import settings
from boto3.dynamodb.types import TypeSerializer
from datetime import datetime, timedelta

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

        epochExipirationTime = datetime.now() + timedelta(days=1)
         
        response = self.client.put_item(
            TableName='link',
            Item = {
                'url' : {
                    'S' : item['url']
                },
                'ttl' : {
                    'N' : str(int(epochExipirationTime.timestamp()))
                },
            }
        )

    
    def is_link_exist(self, url):
        try:
            item = self.client.get_item(hash_key=url)
            return True
        except self.client.dynamodb.exceptions.DynamoDBKeyNotFoundError:
            return False
    
        