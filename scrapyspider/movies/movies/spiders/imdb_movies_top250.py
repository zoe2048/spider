# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy import Request
from ..items import ImdbMovieItem


class ImdbMovieTop250(Spider):
    name = 'imdb_movie_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://www.imdb.com/chart/top/'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        movies = response.xpath('//div[@data-testid="chart-layout-main-column"]//ul[@role="presentation"]/li')
        for movie in movies:
            item = ImdbMovieItem()
            item['ranking'] = movie.xpath('.//div[@class="ipc-metadata-list-summary-item__c"]//a[contains(@href,"title")]/h3/text()').re_first(r'(^\d+)')
            item['movie_name'] = movie.xpath('.//div[@class="ipc-metadata-list-summary-item__c"]//a[contains(@href,"title")]/h3/text()').re_first(r'^\d+.(.*)')
            item['score'] = movie.xpath('.//div[@data-testid="ratingGroup--container"]/span/text()').get()
            item['year_runtime_rated'] = movie.xpath('.//div[@class="sc-43986a27-7 dBkaPT cli-title-metadata"]/span/text()').getall()
            link = movie.xpath('.//div[@class="ipc-metadata-list-summary-item__c"]//a/@href').get()
            next_url = 'https://www.imdb.com' + link
            yield Request(next_url, headers=self.headers, meta={'item': item}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta['item']  # 获取parse()传递的item参数
        tag = response.xpath('//div[@data-testid="genres"]//a[contains(@href,"genres")]/span/text()').getall()
        item['tag'] = ','.join(tag)
        item['info'] = response.xpath('//p[@data-testid="plot"]/span[1]/text()').get()
        country = response.xpath('//li[@data-testid="title-details-origin"]//a[contains(@href,"country")]/text()').getall()
        item['country'] = ','.join(country)
        director = response.xpath('//div[@class="sc-69e49b85-3 dIOekc"]//a[contains(@href,"dr")]/text()').extract()
        item['director'] = ','.join(director)
        yield item

