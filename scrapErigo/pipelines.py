# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class scrapErigoPipeline:
    def process_item(self, item, spider):
        return item

class priceToUsPipeline:
    
    idr_to_usd_rate = 1.4
    
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
    
    
class SavingToMySQLPipelines(object):
    
    def __init__(self):
        self.create_connection()
    
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='erigo_item',
        )
        self.curr = self.conn.cursor()
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        try:
            # Pastikan harga dikonversi ke string jika belum
            price_str = str(item['price'])
            self.curr.execute("""INSERT INTO erigo_cloth (name, price, url) VALUES (%s, %s, %s)""", (
                item['name'],
                price_str,
                item['url'],
            ))
            self.conn.commit()
        except mysql.connector.Error as error:
            print(f"Gagal menyisipkan item: {error}")
            self.conn.rollback()

    
    def close_spider(self, spider):
        self.curr.close()
        self.conn.close()
