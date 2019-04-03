# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IndoNewsFeedItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    datetime = scrapy.Field()
    source = scrapy.Field()
    thumbnail_image_url = scrapy.Field()
    thumbnail_image_alt = scrapy.Field()
    html_content = scrapy.Field()
    text_content = scrapy.Field()
    
