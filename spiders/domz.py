# -*- coding: utf-8 -*-
import scrapy
from store_name.items import StoreNameItem
from scrapy.http import Request
class CrawlSpider(scrapy.Spider):
    name = "domz"
    allowed_domains = ["sh.lianjia.com"]
    start_urls = ['http://sh.lianjia.com/ershoufang']
    page = 1;
    def parse(self, response):
        #print response
        items = []
        item=StoreNameItem()
        #length = len(response.xpath("//*[@id='house-lst']/li[1]/div[2]/h2/a/@href"))
        length = len(response.xpath("//*[contains(@class,'total-price')]/text()"))
        print length
        for i in range(0,length-1):
            name=response.xpath("//*[contains(@class,'row1-text')]/text()")[2*i+1].extract()
            price=response.xpath("//*[contains(@class,'total-price')]/text()")[i].extract()
            comurl=response.xpath("//*[contains(@class,'row2-text')]/a[@class='laisuzhou']/@href")[i].extract()
            fangurl=response.xpath("//*[@class='prop-title']/a/@href")[i].extract()
            comname=response.xpath("//*[contains(@class,'row2-text')]/a[@class='laisuzhou']/span/text()")[i].extract()
            name=name.replace("\t","").replace("\n","").split("|")
            type=name[0]
            area=name[1]
            '''name=response.xpath("//*[@id='house-lst']/li[1]/div[2]/h2/a/@href")[0].extract()
            comname=response.xpath('//*[@id="house-lst"]//*[@class="nameEllipsis"]/text()')[0].extract()
            type=response.xpath('//*[@id="house-lst"]//*[@class="nameEllipsis"]/../following-sibling::*[1]/text()')[0].extract()
            area=response.xpath('//*[@id="house-lst"]//*[@class="nameEllipsis"]/../following-sibling::*[2]/text()')[0].extract()
            price=response.xpath('//*[@id="house-lst"]//*[@class="price"]/span/text()')[0].extract()
            num=response.xpath('//*[@id="house-lst"]//*[@class="square"]//*[@class="num"]/text()')[0].extract()
            fangurl=response.xpath('//*[@id="house-lst"]//div[@class="info-panel"]//*[@name="selectDetail"]/@href')[0].extract()
            comurl=response.xpath('//*[@id="house-lst"]//*[@class="nameEllipsis"]/../@href')[0].extract()
            response.css("");
            item["name"]=name
            item["comname"]=comname
            item["type"]=type
            item["area"]=area
            item["price"]=price
            item["num"]=num
            item["fangurl"]=fangurl
            item["comurl"]=comurl'''
            item["name"]=name
            item["area"]=area
            item["type"]=type
            item["price"]=price
            item["fangurl"]=fangurl
            item["comurl"]=comurl
            item["comname"]=comname
            items.append(item)
            #items.append(item)
            #//*[contains(@class,'row1-text')]/text()
            #//*[contains(@class,'total-price')]/text()
            #//*[contains(@class,'row2-text')]/a[@class='laisuzhou']/@href
            #//*[@class='prop-title']/a/@href
            #name.replace("\t","")
            #name.split("|")
            #
            #//*[@id="js-ershoufangList"]/div[2]/div[3]/div/ul/li[1]/div/div[1]/a
            #0 type
            #1 area
            #'//*[@id="house-lst"]//*[@class="price"]/span'
            #//*[@id="house-lst"]//*[@class="square"]//*[@class="num"]/text()
            #'//*[@id="house-lst"]//div[@class="info-panel"]//*[@name="selectDetail"]/@href') fangurl
            #//*[@id="house-lst"]//*[@class="nameEllipsis"]/../@href comurl
        for item in items:
            yield item
        print(item["name"])
        self.page=self.page+1
        url ="http://sh.lianjia.com/ershoufang/d"+str(self.page)
        if self.page>2:
            return
        else:
            yield Request(url,callback=self.parse)

        #item = StoreNameItem()

