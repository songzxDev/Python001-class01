import scrapy
import pandas as pd
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from myscrapy.items import MyscrapyItem
from _collections import defaultdict


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        item = MyscrapyItem()
        yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse)

    def parse(self, response):
        item = response.meta['item']
        result = defaultdict(list)
        mvs = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl')
        mvname, mvtype, starring, playdate = [], [], [], []
        for mv in mvs:
            mvname = mv.xpath('.//div[1]/div[2]/a/div/div[1]/@title').extract()
            mvtype = mv.xpath('.//div[1]/div[2]/a/div/div[2]/text()').extract()
            starring = mv.xpath('.//div[1]/div[2]/a/div/div[3]/text()').extract()
            playdate = mv.xpath('.//div[1]/div[2]/a/div/div[4]/text()').extract()
        result['mvname'] = [d.strip() for d in mvname if d.strip()][:10]
        result['mvtype'] = [d.strip() for d in mvtype if d.strip()][:10]
        result['starring'] = [d.strip() for d in starring if d.strip()][:10]
        result['playdate'] = [d.strip() for d in playdate if d.strip()][:10]

        item['result'] = result
        yield item
