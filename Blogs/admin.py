from django.contrib import admin
from .models import BlogsCategory,Blog


class BlogsCategoryAdmin(admin.ModelAdmin):
    model = BlogsCategory
    list_display = ['id','name']

class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ['id','title','category','claps','createdAt','author',"postStatus"]


admin.site.register(BlogsCategory,BlogsCategoryAdmin)
admin.site.register(Blog,BlogAdmin)

