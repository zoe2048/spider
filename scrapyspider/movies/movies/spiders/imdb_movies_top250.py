# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy import Request
from ..items import ImdbMovieItem
import json


class ImdbMovieTop250(Spider):
    name = 'imdb_movie_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://www.imdb.com/chart/top/'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        movies_json = response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        movies_info = json.loads(movies_json)
        movies = movies_info['props']['pageProps']['pageData']['chartTitles']['edges']
        for movie in movies:
            item = ImdbMovieItem()
            item['ranking'] = movie['currentRank']
            item['movie_name'] = movie['node']['titleText']['text']
            item['score'] = movie['node']['ratingsSummary']['aggregateRating']
            link = movie['node']['id']
            next_url = 'https://www.imdb.com/title/' + link
            yield Request(next_url, headers=self.headers, meta={'item': item}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta['item']  # 获取parse()传递的item参数
        item['year_rating'] = response.xpath('.//div[@class="sc-af040695-0 iOwuHP"]//a/text()').getall()
        item['runtime'] = response.xpath('.//div[@class="sc-af040695-0 iOwuHP"]//li/text()').get()
        tag = response.xpath('//div[@data-testid="interests"]//a[contains(@href,"interest")]/span/text()').getall()
        item['tag'] = ','.join(tag)
        item['info'] = response.xpath('//p[@data-testid="plot"]/span[1]/text()').get()
        country = response.xpath('//li[@data-testid="title-details-origin"]//a[contains(@href,"country")]/text()').getall()
        item['country'] = ','.join(country)
        director = response.xpath('//div[@class="sc-70a366cc-3 iwmAOx"]//a[contains(@href,"dr")]/text()').extract()
        item['director'] = ','.join(director)
        yield item
