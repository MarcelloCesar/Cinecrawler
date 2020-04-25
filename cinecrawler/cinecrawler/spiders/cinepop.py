# -*- coding: utf-8 -*-
import scrapy
import requests
import psycopg2 as pg
from cinecrawler.items import CinecrawlerItem

class CinepopSpider(scrapy.Spider):
    name = 'cinepop'
    allowed_domains = ['https://cinepop.com.br/noticias']
    start_urls = ['https://cinepop.com.br/noticias/']

    def parse(self, response):
        links = response.xpath("//div[@class='td-module-thumb']/a")

        for link in links:
            href  = link.xpath('@href').extract_first()
            title = link.xpath('@title').extract_first()


            yield CinecrawlerItem(url=href, site="CINEPOP", titulo=title)







