from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from django.core import serializers

from .models import RssFeed, RssEntries
from .forms import RssForm


class IndexView(generic.ListView, generic.FormView):
	form_class = RssForm
	success_url = '/'
	template_name = 'rss/index.html'
	context_object_name = 'feeds'
  

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.save()
		return super(IndexView, self).form_valid(form)
    
	def get_queryset(self):
		return RssFeed.objects.all()

# class RssDetails(generic.DetailView):
# 	model = RssFeed
# 	template_name = "rss/rss_detail.html"


class AllFeedsList(generic.ListView):
	model = RssEntries
	template_name = 'rss/all_feeds.html'
	paginate_by = 20


	def get_context_data(self, **kwargs):
		context = super(AllFeedsList, self).get_context_data(**kwargs)
		context['feeds'] = RssEntries.objects.all()
		context['rss_feeds'] = RssFeed.objects.all()
		return context


class SearchView(generic.ListView):
	model = RssEntries
	template_name = "rss/search.html"
	context_object_name = "obj"

	def get(self, request, *args, **kwargs):
		return render(request, 
			self.template_name, 
			{'authors' : serializers.serialize('json', RssEntries.objects.all(), fields=('author'))},
		)
class RssEntriesDetail(generic.DetailView):
	model = RssEntries
	context_object_name = "obj"
	template_name = "rss/rss_entries_detail.html"

class RssFeedDetail(generic.DetailView):
	model = RssFeed
	
	template_name = 'rss/rss_detail.html'

	def get_context_data(self, **kwargs):
		context = super(RssFeedDetail, self).get_context_data(**kwargs)
		context['rss'] = self.object
		context['rss_feed'] = RssEntries.objects.filter(rss=self.kwargs['pk'])
	
		return context

	





