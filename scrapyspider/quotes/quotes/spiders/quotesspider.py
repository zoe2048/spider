import scrapy
from quotes.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']
    custom_settings = {
        'ITEM_PIPELINES': { 'quotes.mysqlpipelines.QuotesPipeline': 300,}
    }

    def parse(self, response):
        item = QuotesItem()
        for quote in response.css('div.quote'):
            item['content'] = quote.css('span.text::text').extract_first()
            item['author'] = quote.css('small.author::text').get()
            item['tags'] = ','.join(quote.css('div.tags a.tag::text').getall())
            yield item

        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

