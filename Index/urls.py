from django.urls import path
from .views import HomeView
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    def items(self):
        return ['contact', 'quote-maker', 'quote-of-the-day']
    def location(self, item):
        return reverse(item)


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]