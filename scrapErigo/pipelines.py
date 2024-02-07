# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class scrapErigoPipeline:
    def process_item(self, item, spider):
        return item

class priceToUsPipeline:
    
    idr_to_usd_rate = 0.00007143
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        ## check is price present
        if adapter.get('price'):
            
            # converting price to a float
            floatPrice = float(adapter['price'])
            
            # converting the price from gbp to usd using our hand coded exchange rate
            adapter['price'] = floatPrice * self.idr_to_usd_rate
            
            return item
        
        else:
            # drop item if no price
            raise DropItem(f"Missing price in {item}")           
        
        
class DuplicatesPipeline:
    
    def __init__(self):
        self.names_seen = set()
        
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['name'] in self.names_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.names_seen.add(adapter['name'])
            return item
    