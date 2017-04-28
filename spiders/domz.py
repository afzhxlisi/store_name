# -*- coding: utf-8 -*-
import scrapy
from store_name.items import StoreNameItem
from scrapy.http import Request

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class CrawlSpider(scrapy.Spider):
    name = "domz"
    allowed_domains = ["sh.lianjia.com"]
    start_urls = ['http://sh.lianjia.com/ershoufang']
    page = 1;
    count =1;
    total = 1;
    def parse(self, response):
        length = len(response.xpath("//*[contains(@class,'total-price')]/text()"))
        print length
        items = []
        item = StoreNameItem()
        nums=[]

        if(length==0):
            return
        if(self.page==1):
            nums=response.xpath("//ul[@class='content']//span[contains(@class,'num')]/text()")
            totalNum = nums[0].extract()
            self.total = totalNum
            #lastThreeMonSales = nums[1].extract()
            #totalWatchNum = nums[2].extract()
            print totalNum
            #print totalNum
            #typename=response.xpath("//*[@class='m-side-bar']/div/span[@class='header-text']/text()")[0].extract()
            #numType=response.xpath("//*[@class='m-side-bar']/div/span[contains(@class,'c-hollow-tag')]/text()")[0].extract()

            #yield item
            #print item
        nameorgs = response.xpath("//*[contains(@class,'row1-text')]/text()")
        prices = response.xpath("//*[contains(@class,'total-price')]/text()")
        comurls = response.xpath("//*[contains(@class,'row2-text')]/a[@class='laisuzhou']/@href")
        fangurls = response.xpath("//*[@class='prop-title']/a/@href")
        comnames = response.xpath("//*[contains(@class,'row2-text')]/a[@class='laisuzhou']/span/text()")

        for i in range(0, length - 1):
            nameorg=nameorgs[2 * i + 1].extract()
            price=prices[i].extract()
            comurl=comurls[i].extract()
            fangurl=fangurls[i].extract()
            comname=comnames[i].extract()
            name = nameorg.replace("\t", "").replace("\n", "").split("|")
            namefil=""
            for n in name:
                namefil=namefil+n
            type = name[0].replace(" ","")
            area = name[1].replace(" ","").replace("平","")
            item["name"] = namefil
            item["area"] = area
            item["type"] = type
            item["price"] = price
            item["fangurl"] = fangurl
            item["comurl"] = comurl
            item["comname"] = comname
            #if(self.page==1 and i==0):
                #item["totalNum"] = totalNum
                #item["lastThreeMonSales"] = lastThreeMonSales
                #item["totalWatchNum"] = totalWatchNum
                #item["typename"] = typename
                #item["numType"] = numType
            self.count = self.count + 1
            yield item

        self.page = self.page + 1
        url = "http://sh.lianjia.com/ershoufang/d" + str(self.page)
        yield Request(url, callback=self.parse)
