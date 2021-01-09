from rest_framework import serializers
from .models import Blog, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('pk', 'name',)

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('pk','name', 'date', 'title', 'short_desciption', 'responses', 'read_time')