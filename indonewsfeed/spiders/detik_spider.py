# -*- coding: utf-8 -*-
import scrapy
import logging
from bs4 import BeautifulSoup
from indonewsfeed.items import IndoNewsFeedItem
from indonewsfeed.bs_helper import HtmlCleaner

class DetikSpider(scrapy.Spider):
    name = "detik_spider"
    allowed_domains = ["detik.com"]
    start_urls = [
        'https://news.detik.com/indeks'
        ]

    def parse(self, response):
        # get news links
        links = response.xpath('//article//a/@href')
        for link in links:
            if '/berita/' in link.extract():
                yield scrapy.Request(link.extract(), callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        item = IndoNewsFeedItem()
        item["title"] = soup.title.string
        item["link"] = response.url
        item["date"] = self.get_published_date(soup)
        item["desc"] = self.get_news_detail(soup)
        item["source"] = "detik"
        logger = logging.getLogger()
        logger.info("Processing News [Title] : %s" % soup.title.string)
        yield item

    def get_news_detail(self, soup):
        helper = HtmlCleaner()
        content = soup.find("div",{"id":"detikdetailtext"})
        helper.remove_comment(content)
        helper.remove_element(content, 'table')
        helper.remove_element(content, 'script')
        return content.prettify()

    def get_published_date(self, soup):
        published_date = soup.find("div",{"class":"date"})
        return published_date.get_text()

