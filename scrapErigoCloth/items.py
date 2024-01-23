import scrapy

class ErigoCloth(scrapy.Spider):
    name = "Cloth"
    allowed_domains = ['https://erigostore.co.id/']
    start_urls = ["https://erigostore.co.id/collections/all-shirt"]
    
    def parse(self, response):
        urls = response.css
    