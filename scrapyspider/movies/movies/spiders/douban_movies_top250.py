# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from movies.items import DoubanMovieItem
from scrapy import Request
import re


class DoubanMovieTop250(Spider):
    name = 'douban_movie_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanMovieItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        year_pt = re.compile(r'\d+')
        country_pt = re.compile(r'\d+\s/\s(.*)\s/\s')
        dirc_pt = re.compile(r'导演:\s(.*)\s\s\s主演')
        for movie in movies:
            item['ranking'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['score_num'] = movie.xpath('.//div[@class="star"]/span[4]/text()').re(r'(\d+)人评价')[0]
            info = ''.join(movie.xpath('.//div[@class="bd"]/p/text()').extract()).strip()
            year = year_pt.search(info).group()
            country = ''.join(country_pt.findall(info))
            if country == '':
                country = ''.join(re.findall(r'\s/\s(\D+)\s/\s', info))
            director = ''.join(dirc_pt.findall(info))
            item['info'] = info
            item['year'] = year
            item['country'] = country
            item['director'] = director
            yield item

        # 翻页
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)





