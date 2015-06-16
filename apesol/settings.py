# -*- coding: utf-8 -*-

# Scrapy settings for apesol project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

#BOT_NAME = 'apesolweb'

SPIDER_MODULES = ['apesol.spiders']
NEWSPIDER_MODULE = 'apesol.spiders'
DEFAULT_ITEM_CLASS = 'apesol.items.ApesolItem'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'apesol (+http://www.yourdomain.com)'
