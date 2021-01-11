# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from data_scraper.models import Blog


class ScrapyAppPipeline(object):
    def process_item(self, item, spider):
        with open("qqqqqq.txt","w") as f:
            print(item)
            f.write("aa")
        quote = Blog(title=item.get('text'), name=item.get('author'))

        # quote.save()
        return item
