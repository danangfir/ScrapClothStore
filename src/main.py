from spider.erigo import ErigoScrap

if __name__ == "__main__":
    scrap: ErigoScrap = ErigoScrap(search_query="erigo")
    print(scrap.get_pages())
