import imp
from django.contrib import admin
from .models import SubscriberEmail,Contact

class SubscriberEmailAdmin(admin.ModelAdmin):
    model = SubscriberEmail
    list_display = ['id','email',"subscriptionDate"]


class ContactModelAdmin(admin.ModelAdmin):
    list_display=('full_name','email','phone','message')

admin.site.register(SubscriberEmail,SubscriberEmailAdmin)
admin.site.register(Contact,ContactModelAdmin)
