# -*- coding: utf-8 -*-


import scrapy
from quotes.items import AuthorItem


class AuthorSpider(scrapy.Spider):
    name = "author"
    start_urls = ['http://quotes.toscrape.com']
    custom_settings = {
        'ITEM_PIPELINES': { 'quotes.mysqlpipelines.AuthorPipeline': 300,}
    }

    def parse(self, response):
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        item = AuthorItem()

        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        item['name'] = extract_with_css('h3.author-title::text')
        item['birth'] = extract_with_css('.author-born-date::text')
        item['country'] = extract_with_css('.author-born-location::text')
        item['bio'] = extract_with_css('.author-description::text')
        yield item
