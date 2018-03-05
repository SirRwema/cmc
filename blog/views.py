from django.shortcuts import render
from django.http import Http404
from blog.models import BlogPost


def BlogPage(request):
    blog_posts = BlogPost.objects.all()

    return render(request, 'blog/blog.html',{
                'blog_posts':blog_posts,
    })

def Blog_Details(request, id):
    blog_detail = BlogPost.objects.get(id=id)
    return render(request,'blog/blog_details.html',{
            'blog_detail':blog_detail
    })
