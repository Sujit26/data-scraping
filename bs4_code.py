import requests
from bs4 import BeautifulSoup


class BrickSetSpider():
    base_url = 'https://medium.com/tag/'

    def start_requests(self,search_query):
        res = requests.get(self.base_url+search_query)
        return self.parse(res.content)

    def parse(self, content):
        responses = []
        soup = BeautifulSoup(content, "html.parser")

        for article in soup.select('.streamItem.streamItem--postPreview.js-streamItem'):
            name = article.select_one(
                '.ds-link.ds-link--styleSubtle.link.link--darken.link--accent.u-accentColor--textNormal.u-accentColor--textDarken').string
            date = article.select_one('time').string
            title = article.select_one('.graf.graf--title').string
            short_desciption = article.select_one(
                '.graf.graf--trailing').string
            read_time = article.select_one('span.readingTime')['title']
            nor = article.select(
                'a.button.button--chromeless.u-baseColor--buttonNormal')[-1].string
            # if nor.lower()._contains_('read'):
            #     nor = '0 responses'
            formatted_data = {
                'name': name,
                'date': date,
                'title': title,
                'short_desciption': short_desciption,
                'responses': nor,
                'read_time': read_time
            }
            responses.append(formatted_data)
        return responses


if __name__ == '_main_':
    obj = BrickSetSpider()
    obj.start_requests()
