from django.shortcuts import render
from Blogs.models import Blog
from django.views import View
from django.http import JsonResponse
from django.core.paginator import Paginator

import random


class BlogCategoryView(View):
    def get(self, request, blogsCategory):
        return render(request, "pages/category-wise-blogs.html")


def AllBlogs(request):
    blog = Blog.objects.all().filter(postStatus=True).order_by('-id')
    paginator = Paginator(blog, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blogs": page_obj
    }
    return render(request, 'pages/blogs.html', context)


class BlogDetail(View):
    def get(self, request, blogDetail):
        blog = Blog.objects.get(slug=blogDetail)
        # print(blog.tags.all())

        blogList = []
        # in my blog detail  related posts
        # blogs = Blog.objects.all().filter(postStatus=True).filter(category=blog.category)
        # for now all as we donot have more data
        blogs = Blog.objects.all().filter(postStatus=True)
        for i in blogs:
            if len(blogList) < 4:
                i = random.randint(0, len(blogs))
                if Blog.objects.filter(id=i).exists():
                    blg = Blog.objects.get(id=i)
                    if not blg in blogList and not blg == blog:
                        blogList.append(blg)
        context = {
            "blog": blog,
            "related": blogList,
        }
        return render(request, "pages/blogDetails.html", context)


def ClapBlog(request, id):
    blog = Blog.objects.get(id=id)
    blog.claps += 1
    claps = blog.claps
    blog.save()
    return JsonResponse({'claps': claps})


def searchResults(request):
    blogs = Blog.objects.filter(title__icontains=request.GET['q'])
    context = {
        "blogs": blogs,
        "total": len(blogs),
    }
    return render(request, "pages/search.html", context)
