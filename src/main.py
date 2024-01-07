from spider.erigo import ErigoScrap
from spider.helper import FileHelper

if __name__ == "__main__":
    spider = ErigoScrap(search_query="erigo")
    html_content = spider.get_pages()

    # Menggunakan FileHelper untuk menulis konten ke file HTML
    file_helper = FileHelper()
    file_helper.writetmpfile("output.html", html_content)
    