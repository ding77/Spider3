# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LagouSpider(CrawlSpider):
    name = 'qq'
    allowed_domains = ['mail.qq.com']
    start_urls = ['https://mail.qq.com/']

    rules = (
        Rule(LinkExtractor(allow=('cgi-bin/\w*?')),callback='parse_item' ,follow=True),
    )

    def parse_item(self, response):
        '''i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i'''
        people_name=response.css("#list .list_item .list_select span::text").extract()[0]
        email=response.css("#list .list_item .list_select span::text").extract()[1]
        print(people_name)
        print(email)




