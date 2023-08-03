import scrapy
from ..items import FubarItem
from scrapy.loader import ItemLoader


class EbookSpider2(scrapy.Spider):
    name="ebook2"

    start_urls = ["https://books.toscrape.com"]

    def getprice(self, txt):
        return float(txt[1:])

    def extractCSS(self, response):
        debug = False

        ebooks = response.css("article.product_pod")

        if debug: breakpoint()

        for ebook in ebooks:
            # ebookItem = FubarItem()

            loader = ItemLoader(item=FubarItem(),selector=ebook)

            loader.add_css("title", "h3 a::attr(title)")
            # loader.add_xpath() too
            loader.add_css("price", "p.price_color::text")

            # loader.add_value('title', ebook.css("h3 a").attrib["title"])
            # loader.add_value("", ebook.css("p.price_color::text").get())

            # ebookItem['title'] = ebook.css("h3 a::attr(title)").get()
            # title = ebook.css("h3 a").attrib['title']
            # ebookItem['price'] = ebook.css("p.price_color::text").get()

            yield loader.load_item()

    def parse(self, response):
        return self.extractCSS(response)


class EbookSpider(scrapy.Spider):
    name = "ebook"

    start_urls = ["https://books.toscrape.com/"]

    def extractCSS(self, response):
        debug = False

        # Select all "article" tags
        ebooks = response.css("article")

        # ebook data is in article elements, cycle through them
        for ebook in ebooks:
            # Extract title from inner text of anchor (example of selection by tagname)
            title = ebook.css("a::text").get()
            # Extract price from inner text of a "p" with css class type "price_color"
            price = ebook.css("p.price_color::text").get()

            # Example of selection by class alone
            #price = ebook.css(".price_color::text").get()

            # Select by id/name
            # div = ebook.css("#messages").get()

            # Select by attributes ('a' tag with "title" attribute)
            # title = ebook.css("a[title]").get()
            # Same, but specific title
            # title = ebook.css("a[title = 'Soumission']").get()

            if debug:
                breakpoint()

            yield {
                "title": title,
                "price": price
            }

    def extractXPath(self, response):
        # XPath, full path /html/body/yadayada
        # XPath, relative /html//h3
        ebooks = response.xpath("//article")

        for ebook in ebooks:
            title = ebook.xpath(".//a[@title]/text()").get()
            price = ebook.xpath(".//p[@class = 'price_color']/text()").get()

            yield {
                "title": title,
                "price": price
            }

    def parse(self, response):

        #return self.extractCSS(response)
        return self.extractXPath(response)

