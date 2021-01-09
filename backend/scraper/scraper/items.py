# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from mediumScrapper.data_scraper.models import Blog

class BlogItem(DjangoItem):
    django_model = Blog 
