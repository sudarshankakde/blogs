from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from blog.templatetags import extras_filter
from django.core.mail import send_mail
from django_pandas.io import read_frame
from blog.models import Blog, webData, BlogComment,tag
from django.core.paginator import Paginator
from django.http import  JsonResponse
import json
from rest_framework import serializers
from django.db.models import Count
# Create your views here.
data = webData.objects.first()


def AllBlogs(request):
    reponse_data = Blog.objects.order_by('-publish_date').all()
    peginator = Paginator(reponse_data,2)
    page_number = request.GET.get('page',1)
    posts = peginator.get_page(page_number)
    if(request.htmx):
        return render(request, 'card2.html',{'posts':posts})
    return render(request, 'all blogs.html', {'posts': posts, 'data': data, 'index': 'All Blogs'})

def BlogsApi(request):
    reponse_data = Blog.objects.order_by('-publish_date').all().values()
    peginator = Paginator(reponse_data,4)
    page_number = request.GET.get('page',1)
    posts = peginator.get_page(page_number)
    response_data = {'data': list(posts)}
    return JsonResponse(response_data,safe=False)


def detail(request, slug):
    PopularPosts = Blog.objects.order_by('-views')[0:5]
    blogdetails = get_object_or_404(Blog, slug=slug)
    comments = BlogComment.objects.filter(post=blogdetails, parent=None)
    comments = comments.order_by('-sno')
    replies = BlogComment.objects.filter(post=blogdetails).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    blogdetails.views = blogdetails.views + 1
    blogdetails.save()
    return render(request, 'detail.html', {'blog': blogdetails, 'data': data, 'comments': comments, 'replyDict': replyDict, 'moreBlogs': PopularPosts})

def detailApi(request,slug):
    blog = Blog.objects.filter(slug=slug).values()
    blogdetails = get_object_or_404(Blog, slug=slug)
    blogdetails.views = blogdetails.views + 1
    blogdetails.save()
    article_tags_ids = blogdetails.tags.values_list('pk', flat=True)
    similar_published_articles = Blog.objects.filter(tags__in=article_tags_ids)\
                                    .exclude(pk=blogdetails.pk)
    similar_articles = similar_published_articles.annotate(same_tags_in_article=Count('tags'))\
                                .order_by('-same_tags_in_article')[:2].values()
    data = {'data':list(blog),'related':list(similar_articles)}
    return JsonResponse(data,safe=False)

