import scrapy
from scrapy.http import HtmlResponse

class BrickSetSpider(scrapy.Spider):
    name = 'medium'
    base_url = 'https://medium.com/tag/'

    def start_requests(self):
        search_query = 'sql'
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
            nor = data[-1]
            # if nor.lower()._contains_('read'):
            #     nor = '0 responses'
            formatted_data = {
                'name': data[0],
                'date': data[2],
                'title': data[3],
                'short_desciption': data[4],
                'responses': nor,
                'read_time': read_time
            }
            yield formatted_data