from django.db import models
# from Quotes.models import QuotesMaker
from django.urls import reverse


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(null=True,blank=True)
    message = models.TextField()

    def get_absolute_url(self):
     return reverse('contact')

class SubscriberEmail(models.Model):
    email = models.EmailField()
    # userPreferenceCategory = models.ForeignKey(QuotesMaker,on_delete=models.SET_NULL,null=True,blank=True)
    subscriptionDate = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.email
