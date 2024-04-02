from django.shortcuts import render
from django.views import View
from Quotes.models import Quote


class QuoteMaker(View):
    def get(self, request):
        quote = Quote.objects.all().filter(postStatus=True)
        if quote.exists():
            return render(request, "pages/quoteMaker.html", {'quote': quote[0]})
        else:
            return render(request, "pages/404.html")



