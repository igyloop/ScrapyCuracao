import scrapy
from ..items import AmazonpracticaItem

class AmazonSpiderSpider(scrapy.Spider):
    name = "curacao_spider"
    page_number = 2
    start_urls = ["https://www.lacuracao.pe/electrohogar.html?p=1"]

    def parse(self, response):
        items = AmazonpracticaItem()

        product_name = response.css('.product-item-link::text').extract()
        product_brand = response.css('.brand-name::text').extract()
        product_price = response.css('.special-price .price::text').extract()
        product_imagelink = response.css('.product-image-photo::attr(src)').extract()

        items['product_name'] = product_name
        items['product_brand'] = product_brand
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

        next_page = 'https://www.lacuracao.pe/electrohogar.html?p=' + str(AmazonSpiderSpider.page_number)

        if AmazonSpiderSpider.page_number <= 152:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
