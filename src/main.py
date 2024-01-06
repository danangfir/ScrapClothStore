from spider.erigo import ErigoScrap

if __name__ == "__main__":
    spider: ErigoScrap = ErigoScrap(search_query="erigo")
    print(spider.get_pages())

