# -*- coding: utf-8 -*-

import scrapy
from bs4 import BeautifulSoup
from spider.items import NewsMeta, NewsContent
from spider.utils import *
from spider.mongo import mongo_helper

class VoaChineseNewsSpider(scrapy.Spider):
    name = "voachinese"
    site = u'VOA'
    allowed_domains = ["voachinese.com"]
    base_url = "https://www.voachinese.com"
    start_urls = [
            "https://www.voachinese.com/"
    ]

    hheaders = {
        #"authority":"www.voachinese.com",
        #"method":"GET",
        #"path":"/search_product.htm?sort=d&q=apple",
        #"scheme":"https",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "accept-encoding":"gzip, deflate, sdch, br",
        #"accept-language":"zh-CN,zh;q=0.8",
        "upgrade-insecure-requests":"1",
        "Cache-control":"max-age=0",
        #"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Mobile Safari/537.36",
        "referer":"https://www.voachinese.com/",
    }

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        news_list = soup.find_all("div", class_="content")
        items = []
        for news in news_list:
            try:
                a = news.find("a")
                span = news.find("span", class_="title")
                print "href", a.get('href'), type(a.get('href'))
                item = NewsMeta()
                item["site"] = self.site
                item["url"] = self.base_url + a.get('href')
                item["title"] = span.string
                item["datetime"] = now_datetime()

                print item
                #items.append(item)

                req = scrapy.Request(url = item["url"], headers = self.hheaders, callback=self.parse_content)
                req.meta['url'] = item['url']

                yield req
            except Exception as e:
                print e, "|||",  news
                continue
        #return items

    def parse_content(self, response):
        print "parse content"
        soup = BeautifulSoup(response.body, 'lxml')
        ret = []
        try:
            content = soup.find("div", class_="wsw")

            news = NewsContent()
            news['content'] = content.string
            news['url'] = response.meta['url']

            ret.append(news)
        except Exception as e:
            print e, "|||", response.body

        return ret
        pass



