# -*- coding: utf-8 -*-
import scrapy


class SortedPhonesByPriceSpider(scrapy.Spider):
    name = 'sorted_phones_by_price'
    allowed_domains = ['www.emag.ro/telefoane-mobile']
    start_urls = ['http://www.emag.ro/telefoane-mobile/']

    def parse(self, response):
        phone_name = response.xpath("//h2/a/text()").getall()
        price = response.xpath("//div/p[@class='product-new-price']/text()").getall()

        yield {
            'phone_name': phone_name,
            'price': price
        }


