import scrapy
from scrapErigo.itemloaders import scrapErigoLoaders
from scrapErigo.items import scrapErigoProduct

class ErigoScrap(scrapy.Spider):
    # the name of spider
    name = 'scrapErigo'
    allowed_domains = ['erigostore.co.id']
    # these are urls that we will start scraping
    start_urls = ['https://erigostore.co.id/collections/all-shirt']
    
    def parse(self, response):
        products = response.css('li.product')
        
        product_item = scrapErigoProduct()
        for product in products:
            
            erigo = scrapErigoLoaders(item=scrapErigoProduct(), selector=product)
            erigo.add_css('name',"a.card-title::text"),
            erigo.add_css('price','span.price-item::text'),
            erigo.add_css('url','a.card-title::attr(href)'),
            yield erigo.load_item()
            
        next_page = response.css('[rel="next"] ::attr(href)').get()
        
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)
