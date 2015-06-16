# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ApesolPipeline(object):
    def process_item(self, item, spider):
        item['date'] = item['date'].replace('en ', '').replace('- ','')
        return item
