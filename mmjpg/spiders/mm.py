# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mmjpg.items import MmjpgItem


class MmSpider(CrawlSpider):
    name = 'mm'
    allowed_domains = ['mmjpg.com']
    start_urls = ['http://www.mmjpg.com/']
    # start_urls = ['http://www.mmjpg.com/mm/1156']

    rules = (
        Rule(LinkExtractor(allow=r'/home/\d+'), follow=True),
        Rule(LinkExtractor(allow=r'/mm/\d+',restrict_xpaths=r"//div[@class='pic']//li/a"), follow=True),
        Rule(LinkExtractor(allow=r'/\d+/\d+',restrict_xpaths=r"//div[@class='page']//a"), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        item = MmjpgItem()
        item['title'] = response.xpath('//h2/text()').extract_first()
        item['url'] = response.xpath("//div[@id='content']//img/@src").extract_first()
        yield item