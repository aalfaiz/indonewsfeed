# -*- coding: utf-8 -*-
import scrapy
import logging
from datetime import datetime, timezone, timedelta
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
                yield scrapy.Request(link.extract(), callback=self.parse_detail_page_news)

    def parse_detail_page_news(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        item = IndoNewsFeedItem()
        item["title"] = soup.title.string
        item["url"] = response.url
        item["datetime"] = self.get_published_date(soup)
        

        html_news = self.get_html_news_detail(soup)
        clean_html_news = self.get_clean_news_detail(html_news)
        item["html_content"] = html_news.prettify()
        item["text_content"] = clean_html_news.get_text(strip=True).replace('\t','')

        item["thumbnail_image_url"], item["thumbnail_image_alt"] = self.get_thumbnail_image(soup)
        item["source"] = "detik.com"
        logger = logging.getLogger()
        logger.info("Processing News [Title] : %s" % soup.title.string)
        yield item

    def get_html_news_detail(self, soup):
        helper = HtmlCleaner()
        content = soup.find("div",{"id":"detikdetailtext"})
        helper.remove_comment(content)
        helper.remove_element(content, 'table')
        helper.remove_element(content, 'script')
        return content
    
    def get_clean_news_detail(self, soup):
        helper = HtmlCleaner()
        invalid_tags = ['a', 'b', 'br', 'center', 'div', 'strong', 'ins']
        helper.remove_tags_and_get_content(soup, invalid_tags)
        return soup
    
    def get_news_category(self, url):
        if '/berita/' in url:
            return 'politik'


    def get_thumbnail_image(self, soup):
        thumbnail_image = soup.find("div",{"class":"pic_artikel"}).find("img")
        return thumbnail_image["src"], thumbnail_image["alt"]

    def get_published_date(self, soup):
        published_date = soup.find("div",{"class":"date"})
        return self.parse_datestring_to_date_time(published_date.get_text())
    
    def parse_datestring_to_date_time(self, date_string):
        """
        parse datestring with format Day DD mmmm YYYY, HH:mm  example (Senin 29 Oktober 2018, 12:59 WIB)
        """
        date_part = date_string.replace(",","").split(" ")
        day = int(date_part[1])

        # Parse month
        month_name = (date_part[2]).lower()

        month_database = {"januari" : 1, "februari" : 2, "maret" : 3, "april" : 4, "mei" : 5, "juni" : 6, "juli" : 7,
         "agustus" : 8, "september" : 9, "oktober" : 10, "november" : 11, "desember":12}

        month = 0
        if month_name in month_database:
           month = month_database[month_name]
        
        #parse year
        year = int(date_part[3])
        
        #parse hour
        times = date_part[4].split(":")
        hour = int(times[0])
        minute = int(times[1])

        server_datetime = datetime (year, month, day, hour=hour,minute=minute)
        server_datetime = server_datetime - timedelta(hours=7)
        server_datetime = server_datetime.replace(tzinfo = timezone.utc).isoformat()

        return server_datetime
