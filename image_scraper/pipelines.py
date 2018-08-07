# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os, os.path
from scrapy.contrib.pipeline.images import ImagesPipeline
import hashlib
import scrapy

class StoreImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        album_name = item["album_name"]

        for image_url in item["image_urls"]:

            request = scrapy.Request(url=image_url)
            request.meta['album_name'] = album_name
            yield request

        # return [Request(x) for x in item.get(self.images_urls_field, [])]

    def file_path(self, request, response=None, info=None):

        # check if called from image_key or file_key with url as first argument
        url = request.url


        _, image_guid = os.path.split(url)  # change to request.url after deprecation

        path = "{}/{}".format(request.meta["album_name"], image_guid)
        return path

class ImageScraperPipeline(object):
    def process_item(self, item, spider):
        return item
