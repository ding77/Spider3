# -*- coding: utf-8 -*-
import scrapy


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
