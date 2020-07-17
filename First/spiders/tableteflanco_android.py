# -*- coding: utf-8 -*-
import scrapy


class TableteflancoAndroidSpider(scrapy.Spider):
    name = 'tableteflanco_android'
    allowed_domains = ['www.flanco.ro/telefoane-tablete/tablete-si-accesorii/tablete-android.html']
    start_urls = ['http://www.flanco.ro/telefoane-tablete/tablete-si-accesorii/tablete-android.html/']

    def parse(self, response):
        pad_name = response.xpath("//div[@class='produs-title']/a/text()").getall()
        price1 = response.xpath("//div[@class='produs-price']/span/span/text()").getall()
        price_decimal = response.xpath("//div[@class='produs-price']/span/span/sup/text()").getall()

        yield {
            'pad_name': pad_name,
            'price1': price1,
            'price_decimal': price_decimal
        }
