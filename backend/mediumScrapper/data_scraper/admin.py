from django.contrib import admin
from .models import Blog, Tag

class ScraperAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, ScraperAdmin)


admin.site.register(Tag, ScraperAdmin)