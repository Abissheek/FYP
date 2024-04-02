from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.


class QuotesCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, default="")
    img = models.ImageField(default="defaultCategory.png", upload_to="uploads/quote-category")

    def __str__(self):
        return self.name


class Quote(models.Model):
    quote = models.CharField(max_length=400, unique=True)
    backgroundImage = models.ImageField(default="defaultBG.png", upload_to="uploads/quote-images")
    keywords = models.CharField(max_length=400, default="")
    metaDesc = models.CharField(max_length=400, default="")
    category = models.ForeignKey(QuotesCategory, on_delete=models.PROTECT, related_name="quotescategory", null=True,
                                 blank=True)
    tags = TaggableManager()
    author = models.CharField(max_length=100, null=True, blank=True, default="")
    postStatus = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    copyCount = models.IntegerField(default=0)

    def __str__(self):
        return self.quote

    def get_absolute_url(self):
        return reverse('quote-details', args=[str(self.id)])
