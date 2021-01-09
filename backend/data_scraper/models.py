from django.db import models

## models.py
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Blog(models.Model):
    name = models.CharField(max_length=150)
    date = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    short_desciption = models.CharField(max_length=150)
    responses = models.CharField(max_length=150)
    read_time = models.CharField(max_length=150)   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Model"