from django.contrib import admin

from .models import RssFeed, RssEntries


class RssFeedAdmin(admin.ModelAdmin):

    fields =('title', 'active',),
        

# Register your models here.
admin.site.register(RssFeed)
admin.site.register(RssEntries)