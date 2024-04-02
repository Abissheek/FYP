from django.urls import path
from . import views

urlpatterns = [
    path("category/<slug:quotesCategory>/",views.QuoteCategoryView.as_view(),name="quote-category"),
    path("<int:quoteId>/",views.QuoteDetail.as_view(),name="quote-details"),
    path("quote-of-the-day",views.QuoteOfTheDay.as_view(),name="quote-of-the-day"),
    path("give-me-quote/",views.GiveMeQuote,name="give-me-quote"),
    path("like-quote/<int:id>",views.LikeQuote,name='like-quote'),
    path("copy/<int:id>",views.CopyQuoteToSession,name="copy-quote"),
]