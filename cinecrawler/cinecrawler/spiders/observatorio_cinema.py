# -*- coding: utf-8 -*-
import scrapy
from cinecrawler.items import CinecrawlerItem

class ObservatorioCinemaSpider(scrapy.Spider):
    name = 'observatorio_cinema'
    allowed_domains = ['observatoriodocinema.uol.com.br/noticias']
    start_urls = ['http://observatoriodocinema.uol.com.br/noticias/']

    def parse(self, response):
        links = response.xpath("//div[@class='td-block-span6']//h3/a")

        for link in links:
            href = link.xpath('@href').extract_first()
            title = link.xpath('./text()').extract_first()

            yield CinecrawlerItem(url=href, site="CINEPOP", titulo=title)
