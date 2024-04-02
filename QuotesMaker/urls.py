from django.urls import path
from . import views

urlpatterns = [
    path("",views.QuoteMaker.as_view(),name="quote-maker"),
]