# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import psycopg2 as pg

class CinecrawlerPipeline(object):

    def open_spider(self, spider):
        self.db = pg.connect(
            host="192.168.99.101",
            user="user",
            password="senha",
            database="cinecrawler"
        )

        self.cursor = self.db.cursor()


    def close_spider(self, spider):
        self.db.commit()


    def process_item(self, item, spider):
        # verifica se ja foi notificado o item encontrado
        self.cursor.execute("SELECT * FROM LINKS WHERE URL='%s'" % (item['url']))
        if self.cursor.fetchone() is None:
            requests.get("https://api.telegram.org/bot936831786:AAEcz9i8g2FKLWG2j8g5Nf93v-g-y5X3F0A/sendMessage?chat_id=827513381&text=" + item['url'])
            self.cursor.execute("INSERT INTO LINKS(URL, SITE, TITULO) VALUES('%s', '%s', '%s')" % (item['url'], item['site'], item['titulo']))
