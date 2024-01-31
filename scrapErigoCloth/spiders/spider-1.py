import scrapy

class ErigoScrap(scrapy.Spider):
    # nama dari spider
    name = 'erigoSpider'
    # url web yang mau di scrape
    allowed_domains = ['https://erigostore.co.id/']
    starts_url = ['https://erigostore.co.id/collections/all-shirt']
    
    
    def parse(self, response):
        
        # Looping
        products = response.css('li.product')
        for product in products:
            # tambahkan data atau tag web
            yield {
                'name'  : product.css ('a.card-title link-underline card-title-ellipsis').get(),
                'price' : product.css ('span.price-item price-item--sale').get(),
                'url'   : product.css ('div.card-information').attrib['href'],
            }
    
    
    