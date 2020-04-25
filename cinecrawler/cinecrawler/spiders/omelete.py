# -*- coding: utf-8 -*-
import scrapy
from cinecrawler.items import CinecrawlerItem


class OmeleteSpider(scrapy.Spider):
    name = 'omelete'
    allowed_domains = ['https://www.omelete.com.br/noticias']
    start_urls = ['https://www.omelete.com.br/noticias/']
    base_link = "https://www.omelete.com.br"

    def parse(self, response):
        links = response.xpath('//article')

        for link in links:
            href = self.base_link + link.xpath('.//a/@href').extract_first()
            title = link.xpath(".//h2/text()").extract_first()

            yield CinecrawlerItem(url=href, site="OMELETE", titulo=title)


