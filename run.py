# pylint: disable=C0103

from scrapy.crawler import CrawlerProcess
from indonewsfeed.spiders import detik_spider
from scrapy.settings import Settings

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
process.crawl(detik_spider.DetikSpider)
process.start()
