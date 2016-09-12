# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
  url = scrapy.Field()
  title = scrapy.Field()
  featured_image_url = scrapy.Field()
  pass
