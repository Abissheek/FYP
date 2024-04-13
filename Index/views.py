from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from Quotes.models import QuotesCategory,Quote
from Blogs.models import Blog
from Communication.models import SubscriberEmail
import re
import random

# Create your views here.





regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class HomeView(View):
    def get(self,request):
        myCategories = QuotesCategory.objects.all().order_by('-id')
        recentBlogs = Blog.objects.filter(postStatus=True).order_by('-id')

        #recommender logic starts
        userCopiedQUote = getSessionValue(request,'copiedQuoteByUser')
        userLikedQuote = getSessionValue(request,'likedQuoteByUser')
        userVisitedQuoteDetail = getSessionValue(request,'userVisitedDetail')
        userVisitedQuoteCategory = getSessionValue(request,'userVisitedQuoteCategory')

        # Filter quotes based on user behavior
        recommended_quotes = self.filter_quotes_based_on_user_behavior(userCopiedQUote, userLikedQuote,
                                                                       userVisitedQuoteDetail,
                                                                       userVisitedQuoteCategory)


        allquotes = Quote.objects.all().values().filter(postStatus=True)
        # quoteTitle = ""
        recommendedQuotes = []

        for x in range(10):
            if len(recommendedQuotes) < 8:
                i = random.randint(0,len(allquotes))
                if Quote.objects.filter(postStatus=True).filter(id=i).exists():
                    quote = Quote.objects.get(id=i)
                    if not quote in recommendedQuotes:
                        recommendedQuotes.append(quote)
            else:
                break


        context={
            "myCategories" : myCategories,
            'recentBlogs' : recentBlogs,
            'recommendedQuotes' : recommendedQuotes
        }
        return render(request,'pages/index.html',context)




    def post(self,request):
        email = request.POST['email']

        if( email ==''):
            messages.error(request,"Please enter your favourite email")
            return redirect('index')
        else:
            if(re.fullmatch(regex, email)):
                subs = SubscriberEmail(email=email)
                messages.success(request,"Thanks for subscribing Motivative Quotes")
                subs.save()
                return redirect('index')
            messages.error(request,"Please enter valid email")
            return redirect('index')

    def filter_quotes_based_on_user_behavior(self, userCopiedQUote, userLikedQuote, userVisitedQuoteDetail,userVisitedQuoteCategory):
        filtered_quotes = Quote.objects.filter(postStatus=True)
        # Create a list to hold quotes based on user behavior
        recommended_quotes = []
        # copied quote has high priority
        # copied > liked > visited detail of specific quote > visited category
        if userCopiedQUote:
            quoteTitle = userCopiedQUote
        elif userLikedQuote:
            quoteTitle = userLikedQuote
        elif userVisitedQuoteDetail:
            quoteTitle = userVisitedQuoteDetail
        elif userVisitedQuoteCategory:
            quoteTitle = userVisitedQuoteCategory

            # Shuffle the recommended quotes to provide variety
        random.shuffle(recommended_quotes)

        return recommended_quotes[:4]  # Return up to 8 recommended quotes








def getSessionValue(request,key):
    return request.session.get(key)

def setSessionValue(request,key,value):
    request.session[key] = value