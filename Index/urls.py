from django.urls import path
from .views import HomeView
from Communication.views import ContactView
from Blogs.models import Blog
# from Quotes.models import Quote

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


blog_items = {
    'queryset': Blog.objects.all(),
    'date_field': 'createdAt',
}

# quote_items = {
#     'queryset': Quote.objects.all(),
# }

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path("", ContactView.as_view(), name="contact"),
    path('sitemap.xml/', sitemap,
         {
             'sitemaps': {
                 'blog': GenericSitemap(blog_items, priority=0.6, protocol='https', changefreq="weekly"),
                 # 'quote': GenericSitemap(quote_items, priority=0.6, protocol='https', changefreq="weekly"),
                 'static': StaticViewSitemap
             },

         },
         name='django.contrib.sitemaps.views.sitemap'),
]