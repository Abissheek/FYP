from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from tinymce.models import HTMLField

# Create your models here.
class BlogsCategory(models.Model):
    name=models.CharField(max_length=50,unique=True),
    slug = models.SlugField(default=""),

    def __str__(self):
        return self.name


class Blog(models.Model):
    title=models.CharField(max_length=200,unique=True),
    slug= models.SlugField(default=""),
    featuredImage=models.ImageField(default="defaultBG.png",upload_to="uploads/blogImage"),
    keywords=models.CharField(max_length=500,default=""),
    metaDesc=models.CharField(max_length=500,default=""),
    category=models.ForeignKey(
        BlogsCategory,on_delete=models.PROTECT,
        related_name="blogscategory",
        null=True,
        blank=True),
    tags=TaggableManager(),
    body=HTMLField(blank=True,null=True),
    author=models.ForeignKey(User,on_delete=models.PROTECT,related_name="author"),
    createdAt=models.DateTimeField(null=False),
    updated=models.BooleanField(default=False),
    postStatus=models.BooleanField(default=False),


    def __str__(self):
        return self.title,self.metaDesc

    def get_absolute_url(self):
        return reverse('blog-details', args=[str(self.slug)])






