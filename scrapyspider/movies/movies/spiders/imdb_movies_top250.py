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
        url = 'http://www.imdb.com/chart/top'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        movies = response.xpath('//tbody/tr')
        for movie in movies:
            item = ImdbMovieItem()
            item['ranking'] = movie.xpath('.//td[@class="titleColumn"]/text()').re(r'(\d+)')[0]
            item['movie_name'] = movie.xpath('.//td[@class="titleColumn"]/a/text()').extract()[0]
            item['score'] = movie.xpath('.//td[@class="ratingColumn imdbRating"]/strong/text()').extract()[0]
            item['year'] = movie.xpath('.//span[@class="secondaryInfo"]/text()').re(r'\d+')[0]
            link = movie.xpath('.//td[@class="posterColumn"]/a/@href').extract()[0]
            next_url = 'https://www.imdb.com' + link
            yield Request(next_url, headers=self.headers, meta={'item': item}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta['item']  # 获取parse()传递的item参数
        tag = response.xpath('//li[@data-testid="storyline-genres"]//a[contains(@href,"genres")]/text()').extract()
        item['tag'] = ','.join(tag)
        item['info'] = response.xpath('//li[@data-testid="storyline-taglines"]//li//span/text()').extract()
        country = response.xpath('//li[@data-testid="title-details-origin"]//a[contains(@href,"country")]/text()').extract()
        item['country'] = ','.join(country)
        director = response.xpath('//section[@data-testid="title-cast"]//a[contains(@href,"dr")]/text()').extract()
        item['director'] = ','.join(director)
        yield item
