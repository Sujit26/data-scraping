import scrapy
from scrapy.http import HtmlResponse
from scraper.items import BlogItem


class TheodoSpider(scrapy.Spider):
    name = 'medium'
    base_url = 'https://medium.com/tag/'

    def start_requests(self):
        search_query = 'flutter'
        # search_query = 'data-science'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
        }
        yield scrapy.http.Request(
            self.base_url+search_query,
            headers=headers,
            callback=self.parse
        )

    def parse(self, response: HtmlResponse):
        SET_SELECTOR = '.streamItem'
        for article in response.css(SET_SELECTOR):
            data = article.css('a ::text').extract()
            read_time = article.css(
                'span.readingTime ::attr(title)').extract_first()

            print("\n"*5)
            nor = data[-1]
            blog_link = article.css("div.postArticle-readMore a::attr(href)")[-1]
            
            # if nor.lower()._contains_('read'):
            #     nor = '0 responses'

            item = BlogItem()
            
            item['name '] = data[0]
            item['date '] = data[2]
            item['title '] = data[3]
            item['short_desciption'] = data[4]
            item['responses '] = nor
            item['read_time'] = read_time

            # formatted_data = {
            #     'name': data[0],
            #     'date': data[2],
            #     'title': data[3],
            #     'short_desciption': data[4],
            #     'responses': nor,
            #     'read_time': read_time,
            #     # "blog_link": blog_link
            # }
            
            yield item