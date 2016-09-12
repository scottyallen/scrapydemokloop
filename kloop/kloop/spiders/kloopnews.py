# -*- coding: utf-8 -*-
import scrapy

import re

from kloop.items import NewsItem

class KloopnewsSpider(scrapy.Spider):
  name = "kloopnews"
  allowed_domains = ["kloop.kg"]
  start_urls = (
    'http://kloop.kg/blog/category/novosti/',
  )

  def parse(self, response):
    urls = response.xpath("//h3[@class='entry-title td-module-title']/a/@href").extract()
    for url in urls:
      req = scrapy.Request(url, callback=self.parse_article)
      yield req
    match = re.search(r'page/(\d+)', response.url)
    if match:
      current_page = int(match.group(1))
      if current_page > 20:
        return
      next_page_url = 'http://kloop.kg/blog/category/novosti/page/%d/' % (current_page + 1)
    else:
      next_page_url = 'http://kloop.kg/blog/category/novosti/page/2/'

    req = scrapy.Request(next_page_url, callback=self.parse)
    yield req
  
  def parse_article(self, response):
    item = NewsItem()
    item['url'] = response.url
    item['title'] = first(response.xpath("//h1[@class='entry-title']/text()").extract())
    item['featured_image_url'] = first(response.xpath("//div[@class='td-post-featured-image']//img/@src").extract())
    yield item

def first(input):
  if len(input) > 0:
    return input[0]
  else:
    return None
