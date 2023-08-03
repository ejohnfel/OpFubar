import scrapy


class PackteBook(scrapy.Spider):
    name = "packtebook"

    url = "https://www.packtpub.com/free-learning"

    def parse(self, response):
        pass

