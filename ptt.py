# -*- coding: utf-8 -*-
import scrapy


class PttSpider(scrapy.Spider):
    name = 'ptt'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/index.html/']

    def parse(self, response):
        print("*"*20,response)
        input("TEST")
        pass
