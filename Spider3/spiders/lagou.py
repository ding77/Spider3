# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['http://www.lagou.com/']

    rules = (
        Rule(LinkExtractor(allow=('zhaopin/.*')) ,follow=True),
        Rule(LinkExtractor(allow=('gongsi/\d+.html')), follow=True),
        Rule(LinkExtractor(allow=('jobs/\d+.html')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        '''i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i'''
        name = response.css('.position-head .job-name span::text').extract()[0]
        salary = response.css(".job_request p span::text").extract()[0]
        id = response.css(".job_request p span::text").extract()[1]
        work = response.css(".job_request p span::text").extract()[2]
        school = response.css(".job_request p span::text").extract()[3]
        type = response.css(".job_request p span::text").extract()[4]
        workplace = response.css(".work_addr a::text").extract()
        workplace=''.join(workplace)
        introduce = response.css('.job_bt div p::text').extract()
        introduce = ''.join(introduce)



        print(name)
        print(salary)
        print(id)
        print(work)
        print(school)
        print(type)
        print(workplace)

