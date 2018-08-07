# -*- coding: utf-8 -*-

# Scrapy settings for image_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from image_scraper.pipelines import StoreImgPipeline

BOT_NAME = 'image_scraper'

SPIDER_MODULES = ['image_scraper.spiders']
NEWSPIDER_MODULE = 'image_scraper.spiders'

ITEM_PIPELINES = {'image_scraper.pipelines.StoreImgPipeline': 1}

# Wherever you want to store it
IMAGES_STORE = ""
FILES_STORE = ""

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

