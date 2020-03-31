# -*- coding: utf-8 -*-
import scrapy
import requests


class CinepopSpider(scrapy.Spider):
    name = 'cinepop'
    allowed_domains = ['https://cinepop.com.br/noticias']
    start_urls = ['https://cinepop.com.br/noticias/']

    def parse(self, response):
        links = response.xpath("//div[@class='td-module-thumb']/a")
        with open("teste.txt", "w") as file:
            for link in links:
                href  = link.xpath('@href').extract_first()
                title = link.xpath('@title').extract_first()

                file.write(href + ' | ' + title + "\n")

                requests.get("https://api.telegram.org/bot936831786:AAEcz9i8g2FKLWG2j8g5Nf93v-g-y5X3F0A/sendMessage?chat_id=827513381&text=" + href)
                exit()



