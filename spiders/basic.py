# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["spider"]
    start_urls = ['http://spider/']

    def parse(self, response):
        pass
