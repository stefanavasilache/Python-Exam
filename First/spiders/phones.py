# -*- coding: utf-8 -*-
import scrapy
from scrapy import Item, Field

class Article(Item):
    phone_name = Field()
    prices = Field()
    total = Field()

class PhonesSpider(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['www.emag.ro/telefoane-mobile']
    start_urls = ['http://www.emag.ro/telefoane-mobile/']



    def parse(self, response):

        item = Article()
        phone_name = response.xpath("//h2/a/text()").getall()
        prices = response.xpath("//div/p[@class='product-new-price']/text()").getall()
        total = response.xpath("//h2/a/text()").getall()

        item['phone_name'] = phone_name
        item['prices'] = prices


        for a in response.xpath("//div[@class='card']").getall():
            item['prices'] = "".join( response.xpath("//div/p[@class='product-new-price']/text()").getall())




        return item


