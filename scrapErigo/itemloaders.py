
from scrapy.loader import itemloaders

class scrapErigoLoader(itemloaders):
    
    price_in = mapCompose(lambda x : x.split())
    
    pass