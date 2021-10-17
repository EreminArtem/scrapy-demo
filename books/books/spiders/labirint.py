import scrapy
from scrapy.http import HtmlResponse

from books.books.items import BookItem


class LabirintSpider(scrapy.Spider):
    name = 'labirint'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/books/']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath('//a[@class="pagination-next__text"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath('//a[@class="product-title-link"]/@href').getall()
        for link in links:
            yield response.follow(link, callback=self.book_parse)

    def book_parse(self, response: HtmlResponse):
        title = response.xpath('//h1/text()').get()
        main_price = response.xpath('//span[@class="buying-priceold-val-number"]/text()').get()
        special_price = response.xpath('//span[@class="buying-pricenew-val-number"]/text()').get()
        rate = response.xpath('//div[@id="rate"]').get()
        yield BookItem(
            title=title,
            main_price=main_price,
            special_price=special_price,
            rate=rate
        )
