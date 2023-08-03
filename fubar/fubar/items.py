# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst


def getprice(self, txt):
    return float(txt[1:])


class FubarItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = Field(output_processor=TakeFirst())
    price = Field(
        input_processer=MapCompose(getprice),
        output_processor=TakeFirst()
                  )
