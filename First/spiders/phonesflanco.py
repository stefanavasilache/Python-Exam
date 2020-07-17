# -*- coding: utf-8 -*-
import scrapy


class PhonesflancoSpider(scrapy.Spider):
    name = 'phonesflanco'
    allowed_domains = ['www.flanco.ro/telefoane-tablete/smartphone.html']
    start_urls = ['http://www.flanco.ro/telefoane-tablete/smartphone.html/']

    def parse(self, response):
        phone_name = response.xpath("//div[@class='produs-title']/a/text()").getall()
        price1 = response.xpath("//div[@class='produs-price']/span/span/text()").getall()
        price_decimal = response.xpath("//div[@class='produs-price']/span/span/sup/text()").getall()

        yield {
            'phone_name': phone_name,
            'price1': price1,
            'price_decimal' : price_decimal
        }
