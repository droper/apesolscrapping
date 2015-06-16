# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class ApesolItem(Item):
    title = Field()
    date = Field()
    desc = Field()
    username = Field()


