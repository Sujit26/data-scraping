# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse
import scrapy
from data_scraper.models import Blog


class IcrawlerSpider(CrawlSpider):
    name = 'icrawler'
    base_url = 'https://medium.com/tag/'

    def __init__(self, *args, **kwargs):
        # We are going to pass these args from our django view.
        # To make everything dynamic, we need to override them inside __init__ method
        self.url = kwargs.get('url')
        tag = kwargs.get("tag")
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
        }

        print("........")
        scrapy.http.Request(
            self.base_url+tag,
            headers=headers,
            callback=self.parse
        )

        IcrawlerSpider.rules = [
           Rule(LinkExtractor(unique=True), callback='parse_item'),
        ]
        super(IcrawlerSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        # You can tweak each crawled page here
        # Don't forget to return an object.
        i = {}
        i['url'] = response.url
        return i


    def parse(self, response: HtmlResponse):
        with open("filemanrdasa.txt","w+") as f:
            f.write("aya")
            
        SET_SELECTOR = '.streamItem'
        print("****")
        for article in response.css(SET_SELECTOR):
            data = article.css('a ::text').extract()
            read_time = article.css(
                'span.readingTime ::attr(title)').extract_first()
            print("\n"*5)
            nor = data[-1]
            blog_link = article.css("div.postArticle-readMore a::attr(href)")[-1]
            
            # if nor.lower()._contains_('read'):
            #     nor = '0 responses'

            # item = BlogItem()
            # item['name '] = data[0]
            # item['date '] = data[2]
            # item['title '] = data[3]
            # item['short_desciption'] = data[4]
            # item['responses '] = nor
            # item['read_time'] = read_time

            formatted_data = {
                'name': data[0],
                'date': data[2],
                'title': data[3],
                'short_desciption': data[4],
                'responses': nor,
                'read_time': read_time,
                # "blog_link": blog_link
            }

            # obj,_ = Blog.objects.get_or_create(title = data[3])
            # obj.name = data[0]
            # obj.date = data[2]
            # obj.short_desciption = data[4]
            # obj.responses = nor
            # obj.read_time = read_time
            # obj.save()
            # print(obj)

            
            yield formatted_data
