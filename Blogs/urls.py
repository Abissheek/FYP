from django.urls import path
from . import views

urlpatterns = [
    path("category/<slug:blogsCategory>",views.BlogCategoryView.as_view(),name="blog-category"),
    path("all/",views.AllBlogs,name="all-blogs"),
    path("search/",views.searchResults,name="search"),
    path("<slug:blogDetail>",views.BlogDetail.as_view(),name="blog-details"),
    path("clap-blog/<int:id>/",views.ClapBlog,name='clap-blog'),
]

