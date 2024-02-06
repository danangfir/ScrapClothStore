import scrapy
from scrapErigo.items import scrapErigoItem

class ErigoScrap(scrapy.Spider):
    name = 'scrapErigo'
    allowed_domains = ['erigostore.co.id']
    start_urls = ['https://erigostore.co.id/collections/all-shirt']
    
    def parse(self, response):
        products = response.css('li.product')
        
        product_item = scrapErigoItem
        for product in products:
            
            product_item['name'] = product.css('a.card-title::text').get(),
            product_item['price'] = product.css('span.price-item::text').get(),
            product_item['url'] = product.css('a.card-title::attr(href)').get(),  # Pastikan selector ini benar
            yield product_item
            
        next_page = response.css('[rel="next"] ::attr(href)').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)
