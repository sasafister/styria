from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name="index"),
	url(r'^(?P<pk>\d+)/$', views.RssEntriesDetail.as_view(), name="entries_detail"),
	url(r'^all/$', views.AllFeedsList.as_view(), name="all"),
	url(r'^search/$', views.SearchView.as_view(), name="search"),
	# url(r'^(?P<pk>\d+)/$', views.RssDetails.as_view(), name='detail'),
	url(r'^feed/(?P<pk>\d+)/$', views.RssFeedDetail.as_view(), name="feed_detail"),
]