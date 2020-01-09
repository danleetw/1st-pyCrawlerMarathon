# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path
from pprint import pprint
from ..items import PostItem
import logging
from scrapy.http import FormRequest

import time

#爬蟲主體，定義如何抓取需要的數據
#https://city.shaform.com/zh/2016/02/28/scrapy/ #自動回答年齡問題
#https://ithelp.ithome.com.tw/articles/10205893 #[Day 13] 實戰：Scrapy爬PTT文章

'''
scrapy.cfg：基礎設置
items.py：抓取條目的結構定義
middlewares.py：中間件定義
pipelines.py：管道定義，用於抓取數據後的處理
settings.py：全局設置
spiders\PTTCrawler.py：爬蟲主體，定義如何抓取需要的數據
'''
    



# 範例目標網址: https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html
class PttcrawlerSpider(scrapy.Spider):
    #----SCRAPY的ID
    name = 'PttCrawler' 
    
    #允許爬的網址清單
    allowed_domains = ['ptt.cc'] 
    
    #開始位置
    start_urls = ['https://www.ptt.cc/bbs/Gossiping/index.html',]
    cookies = {'over18': '1'}
    

    _pages=0
    _retries = 0
    MAX_RETRY = 3



    def __init_(self,url=None,target_file_name=None):
        self.url=url
        self.target_file_name=target_file_name
        
    #---發動Request
    def start_requests(self):
        
        
        for url in self.start_urls:
            #print("!!!!"," Start Request")
            #print("url:",url)
            #input("A")
            yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies)
            #yield scrapy.Request(url=url, callback=self.parse)
            
        
    def parse(self, response):
        
        #print("Len:",len(response.css("div.over18-notice")))
        #input("Parse!!!!")
        #------判斷是否Over 18 Year Old============================
        #<div class="over18-notice">
        #print(len(response.xpath('//div[@class="over18-notice"]')))
        #if len(response.css("div.over18-notice"))>0:
        #if len(response.xpath('//div[@class="over18-notice"]'))>0:
        #    #print("詢問是否18歲!")
        #    if self._retries < PttcrawlerSpider.MAX_RETRY:
        #        self._retries += 1
        #        #logging.warning('第 {} 次，嘗試登入..'.format(self._retries))
        #        #----按Yes
        #        yield FormRequest.from_response(response,
        #                                        formdata={'yes': 'yes'},
        #                                        callback=self.parse)
        #    else:
        #        logging.warning('登入不成功')
        
        #print(response.body)
        #input("##############################")
        #self._pages += 1
        print(len(response.css('div.r-ent')))
        items=list()
        for tag in response.css('div.r-ent'):
            items=list()
            item=PostItem()
            item['title'] = tag.css("div.title a::text").extract_first()
            item['url']   = tag.css('div.title a::attr(href)').extract_first()
            item['author'] = tag.css('div.author::text').extract_first()
            item['date'] = tag.css('div.date::text').extract_first()
            item['push'] = tag.css('span::text').extract_first()
            #items.append(item)
            yield item
        
            
                #yield item
            #return    
            #print(items)
           
                
                #item['title'] = tag.css("div.title a::text")[0].extract()
                #item['url']   = tag.css('div.title a::attr(href)')[0].extract()
                #item['author'] = tag.css('div.author::text')[0].extract()
                #item['date'] = tag.css('div.date::text')[0].extract()
                #item['push'] = tag.css('span::text')[0].extract()
                
                
                #print(item)
                
            #for href in response.css('.r-ent > div.title > a::attr(href)'):
            #    print("!!!Href:",href)
            #    #print("Href:",href.extract())
                
        


        
        #print("#"*20," Start ","#"*20)
              
        #for i in range(1):
        #    time.sleep(1)
        #    
        #i=0
        #url = "https://www.ptt.cc/bbs/Gossiping/index" + str(39016 - i) + ".html"
        #    #yield scrapy.Request (url, cookies={'over18': '0'}, callback=self.parse_article)
        #yield scrapy.Request (url,  callback=self.parse_article)
        
        
        #print("#"*20," End ","#"*20)
        
    def parse_article(self, response):
        return
        print("#"*20," Start Parse_article ","#"*20)
        item = PostItem()
        target = response.css("div.r-ent")
    
    
        for tag in target:
            try:
                item['title'] = tag.css("div.title a::text")[0].extract()
                item['url']   = tag.css('div.title a::attr(href)')[0].extract()
                item['author'] = tag.css('div.author::text')[0].extract()
                item['date'] = tag.css('div.date::text')[0].extract()
                item['push'] = tag.css('span::text')[0].extract()
                
    
                yield item
    
            except IndexError:
                pass
            continue
        print("#"*20," End Parse_article ","#"*20)