from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from django.urls import reverse


class BlogsCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(default="")

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(default="")
    featuredImage = models.ImageField(default="defaultBG.png", upload_to="uploads/blog-images")
    keywords = models.CharField(max_length=400, default="")
    metaDesc = models.CharField(max_length=400, default="")
    category = models.ForeignKey(BlogsCategory, on_delete=models.PROTECT, related_name="blogscategory", null=True,blank=True)
    tags = TaggableManager()
    body = HTMLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="author")
    createdAt = models.DateField(null=True)
    updated = models.BooleanField(default=False)
    postStatus = models.BooleanField(default=False)
    claps = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-details', args=[str(self.slug)])
