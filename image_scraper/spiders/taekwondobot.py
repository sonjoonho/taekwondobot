# -*- coding: utf-8 -*-
import scrapy
from image_scraper.items import ImageScraperItem
from urllib.parse import urljoin


class TaekwondobotSpider(scrapy.Spider):
    name = 'taekwondobot'
    allowed_domains = ['localhost']
    start_urls = ["http://127.0.0.1:4000/photo"]

    def parse(self, response):
        albums = response.xpath('//*[@id="content"]/div/a/@href').extract()
        for album in albums:
            url = urljoin("http://localhost:4000", album)
            yield scrapy.Request(url, callback=self.parse_album)


    def parse_album(self, response):
        images = response.xpath('//*[@class="album"]/a/@href').extract()
        images = [urljoin("http://localhost:4000", image) for image in images]
        album_name = response.xpath('//*[@id="splash"]/div/h2')

        print(images)

        item = ImageScraperItem()

        item["album_path"] = album_name.replace(" ", "")

        item["image_urls"] = images
        yield item

