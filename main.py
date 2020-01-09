# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def main():
    target_urls=[
            'https://www.ptt.cc/bbs/Gossiping/index.html'
            ]
    target_file_name="test1.json"
    
    process=CrawlerProcess(get_project_settings())
    process.crawl('PttCrawler',url=target_urls,target_file_name=target_file_name)
    process.start()


if __name__== '__main__':
    main()    