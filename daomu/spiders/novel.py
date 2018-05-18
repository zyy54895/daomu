# -*- coding: utf-8 -*-
import scrapy
from daomu.items import DaomuItem

class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['seputu.com']
    start_urls = ['http://seputu.com/']

    def parse(self, response):
        contents = response.xpath('//div[@class="mulu-title"]//h2/text()').extract()
        for content in contents:
            chapter_titles = response.xpath('//div[@class="mulu-title"]//h2[text()="' + content + '"]/ancestor::*/div[@class="box"]//a/text()').extract()
            for chapter_title in chapter_titles:
                chapter_url = response.xpath('//div[@class="box"]//a[text()="' + chapter_title + '"]/@href').extract()
                #print(content, chapter_title, chapter_url)
                item = DaomuItem(content=content, chapter_title=chapter_title, chapter_url=chapter_url)
                yield item