from __future__ import unicode_literals
from django.utils.encoding import smart_unicode

from django.db import models

# Create your models here.
class RssFeed(models.Model):
	title = models.CharField(max_length=255)
	link = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)

	def __unicode__(self): 
		return smart_unicode(self.title)

class RssEntries(models.Model):
	rss = models.ForeignKey(RssFeed, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	link = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	image = models.CharField(max_length=255)
	published = models.CharField(max_length=255)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-published"]