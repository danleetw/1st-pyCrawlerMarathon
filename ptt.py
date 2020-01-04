# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class PttSpider(scrapy.Spider):
    name = 'ptt'
    allowed_domains = ['http://www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/index.html']
    start_urls = ['https://www.ptt.cc/bbs/movie/index.html']
    

    def parse(self, response):
        #print(response.text)
        
        res=BeautifulSoup(response.body)
        print("*"*80)
        for title in res.select('.r-ent'):
            print(title.select(".title")[0].select("a"))
        print("*"*80)   
        pass
