import scrapy

class ErigoScrap(scrapy.Spider):
    name = 'erigoSpider'
    allowed_domains = ['erigostore.co.id']
    start_urls = ['https://erigostore.co.id/collections/all-shirt']
    
    def parse(self, response):
        products = response.css('li.product')
        for product in products:
            yield {
                'name': product.css('a.card-title::text').get(),
                'price': product.css('span.price-item::text').get(),
                'url': product.css('a.card-title::attr(href)').get(),  # Pastikan selector ini benar
            }
            
        next_page = response.css('[rel="next"] ::attr(href)').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)
