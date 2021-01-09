from scrapy_djangoitem import DjangoItem
from .models import Blog

class BlogItem(DjangoItem):
    django_model = Blog