
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
import re
import random

class HomeView(View):
    def get(self, request):
        return render(request, 'pages/index.html')

def getSessionValue(request, key):
    return request.session.get(key)


def setSessionValue(request, key, value):
    request.session[key] = value