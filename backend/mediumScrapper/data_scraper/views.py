from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets

class BlogApiView(APIView):
    
    def get(self,request,tag):
        print(tag)
        
        data = Blog.objects.all()
        serializer = BlogSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)


