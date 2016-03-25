from django import forms
from django.forms import TextInput

from .models import RssFeed

# class RssForm(forms.Form):
# 	title = forms.CharField()
# 	time = forms.DateTimeField()
# 	link = forms.CharField()
# 	author = forms.CharField()
# 	image = forms.CharField()

class RssForm(forms.ModelForm):

	# title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# link = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta:
		model = RssFeed
		fields = ('title', 'link')
		widgets = {
			'title': TextInput(attrs={'class' : 'form-control'}),
			'link': TextInput(attrs={'class' : 'form-control'})
		}