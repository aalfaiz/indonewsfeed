# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from indonewsfeed.items import IndoNewsFeedItem

class DetikSpider(scrapy.Spider):
    name = "detik_spider"
    allowed_domains = ["detik.com"]
    start_urls = [
        'https://news.detik.com/indeks',
        'https://news.detik.com/indeks/all?date=07%2F12%2F2018'
        ]

    def parse(self, response):
        print("masuk %s" % response.url)

        # get news links
        links = response.xpath('//article//a/@href')
        for link in links:
            yield scrapy.Request(link.extract(), callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        print("masuk detail page : %s" % response.url)
        soup = BeautifulSoup(response.text, 'lxml')

        item = IndoNewsFeedItem()
        item["title"] = soup.title.string
        item["link"] = response.url
        item["date"] = ""
        item["desc"] = ""
        item["source"] = "detik"
        print("Judul : %s" % soup.title.string)

        yield item
