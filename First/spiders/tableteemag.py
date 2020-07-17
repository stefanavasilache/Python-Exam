# -*- coding: utf-8 -*-
import scrapy


class TableteemagSpider(scrapy.Spider):
    name = 'tableteemag'
    allowed_domains = ['www.emag.ro/tablete']
    start_urls = ['http://www.emag.ro/tablete/']

    def parse(self, response):
        pad_name = response.xpath("//h2/a/text()").getall()
        price = response.xpath("//div/p[@class='product-new-price']/text()").getall()

        yield {
            'pad_name': pad_name,
            'price': price
        }
