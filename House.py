import scrapy
class House(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    id = scrapy.Field()
    gardenId = scrapy.Field()