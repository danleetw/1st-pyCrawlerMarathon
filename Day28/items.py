# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

#items.py
#抓取條目的結構定義


import scrapy


class PostItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    push = scrapy.Field()
    


class BooksItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
