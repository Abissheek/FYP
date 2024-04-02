from django.shortcuts import render, redirect
from Index.views import setSessionValue
from django.views import View
from .models import QuotesCategory, Quote
from django.http import JsonResponse

import random


class QuoteCategoryView(View):
    def get(self, request, quotesCategory):
        try:
            category = QuotesCategory.objects.get(slug=quotesCategory)
            quotesWithThisCategory = category.quotescategory.all().filter(postStatus=True).order_by('-id')
            i = random.randint(0, len(quotesWithThisCategory))
            if Quote.objects.filter(id=i).exists():
                quote = Quote.objects.get(id=i)
                setSessionValue(request, 'userVisitedQuoteCategory', quote.quote)
            else:
                pass
                setSessionValue(request, 'userVisitedQuoteCategory', quotesWithThisCategory[0].quote)

            context = {
                "allquotes": quotesWithThisCategory,
                'category': category
            }
            return render(request, "pages/category-wise-quotes.html", context)

        except:
            return redirect('index')


class QuoteDetail(View):
    def get(self, request, quoteId):
        try:
            quote = Quote.objects.get(id=quoteId)
            # print(quote.tags.all())
            setSessionValue(request, 'userVisitedDetail', quote.quote)

            context = {
                'quote': quote
            }
            return render(request, "pages/quoteDetails.html", context)

        except:
            return redirect('index')


class QuoteOfTheDay(View):
    def get(self, request):
        quote = Quote.objects.filter(postStatus=True).filter(category=1)
        i = random.randint(0, len(quote))
        quoteOfTheDay = ""
        if Quote.objects.filter(id=i).exists():
            quoteOfTheDay = Quote.objects.get(id=i)
        else:
            return render(request, "pages/404.html")

        context = {
            'quote': quoteOfTheDay.quote,
            'author': quoteOfTheDay.author
        }
        return render(request, "pages/quoteOfTheDay.html", context)


def GiveMeQuote(request):
    quote = Quote.objects.filter(postStatus=True).filter(category=1)
    i = random.randint(0, len(quote))
    quoteOfTheDay = ""
    if Quote.objects.filter(id=i).exists():
        quoteOfTheDay = Quote.objects.get(id=i)
    else:
        return render(request, "pages/404.html")

    context = {
        'quote': quoteOfTheDay.quote,
        'author': quoteOfTheDay.author
    }
    return JsonResponse(context)


def LikeQuote(request, id):
    # Get the quote object
    quote = Quote.objects.get(id=id)
    if 'likedQuoteByUser' in request.session and request.session['likedQuoteByUser'] == quote.quote:
        quote.likes -= 1
        del request.session['likedQuoteByUser']
    else:
        # If not already liked, increment the likes count
        quote.likes += 1
        # Set the session value to indicate liking
        request.session['likedQuoteByUser'] = quote.quote

    # Save the changes to the quote object
    quote.save()

    # Return the updated likes count
    return JsonResponse({'likes': quote.likes})


def CopyQuoteToSession(request, id):
    quote = Quote.objects.get(id=id)
    quote.copyCount += 1
    quote.save()
    setSessionValue(request, 'copiedQuoteByUser', quote.quote)
    return JsonResponse({'copy': quote})