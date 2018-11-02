# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy import Request
from movies.items import ImdbMovieItem


class ImdbMovieTop250(Spider):
    name = 'imdb_movie_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }

    def start_requests(self):
        url = 'http://www.imdb.com/chart/top'
        yield Request(url,headers=self.headers)

    '''
    def parse(self, response):
        item = ImdbMovieItem()
        movies = response.xpath('//tbody/tr')
        for movie in movies:
            item['ranking'] = movie.xpath('.//td[@class="titleColumn"]/text()').re(r'(\d+)')[0]
            item['movie_name'] = movie.xpath('.//td[@class="titleColumn"]/a/text()').extract()[0]
            item['score'] = movie.xpath('.//td[@class="ratingColumn imdbRating"]/strong/text()').extract()[0]
            yield item
    '''

    def parse(self, response):
        #item = ImdbMovieItem()
        movies = response.xpath('//tbody/tr')
        for movie in movies:
            item = ImdbMovieItem()
            item['ranking'] = movie.xpath('.//td[@class="titleColumn"]/text()').re(r'(\d+)')[0]
            item['movie_name'] = movie.xpath('.//td[@class="titleColumn"]/a/text()').extract()[0]
            item['score'] = movie.xpath('.//td[@class="ratingColumn imdbRating"]/strong/text()').extract()[0]
            link = movie.xpath('.//td[@class="posterColumn"]/a/@href').extract()[0]
            next_url = 'https://www.imdb.com' + link
            yield Request(next_url,headers=self.headers,meta={'item':item},callback=self.parse_detail)


    def parse_detail(self,response):
        item = response.meta['item'] #获取parse()传递的item参数
        item['tag'] = response.xpath('//div[@class="subtext"]//a[contains(@href,"search")]/text()').extract()
        yield item









