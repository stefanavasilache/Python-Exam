# -*- coding: utf-8 -*-
import scrapy


class TableteflancoIosSpider(scrapy.Spider):
    name = 'tableteflanco_ios'
    allowed_domains = ['www.flanco.ro/telefoane-tablete/tablete-si-accesorii/tablete-ios.html']
    start_urls = ['http://www.flanco.ro/telefoane-tablete/tablete-si-accesorii/tablete-ios.html/']

    def parse(self, response):
        phone_name = response.xpath("//div[@class='produs-title']/a/text()").getall()
        price1 = response.xpath("//div[@class='produs-price']/span/span/text()").getall()
        price_decimal = response.xpath("//div[@class='produs-price']/span/span/sup/text()").getall()

        yield {
            'phone_name': phone_name,
            'price1': price1,
            'price_decimal': price_decimal
        }