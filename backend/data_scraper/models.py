from django.db import models

## models.py
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class Blog(models.Model):
    name = models.CharField(max_length=150,blank=True ,null=True)
    date = models.CharField(max_length=150,blank=True ,null=True)
    title = models.CharField(max_length=150,unique=True)
    short_desciption = models.CharField(max_length=150,blank=True ,null=True)
    responses = models.CharField(max_length=150,blank=True ,null=True)
    read_time = models.CharField(max_length=150,blank=True ,null=True)
    tag = models.CharField(max_length=150,default="blog")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Model"