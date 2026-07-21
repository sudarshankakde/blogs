from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from blog.templatetags import extras_filter
from django.core.mail import send_mail
from django_pandas.io import read_frame
from blog.models import Blog, webData, BlogComment, tag
from django.db import models
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from rest_framework import serializers
from django.db.models import Count
# Create your views here.
def get_web_data():
    return webData.objects.first()


def AllBlogs(request):
    if request.user.is_superuser:
        reponse_data = Blog.objects.order_by('-publish_date').all()
    else:
        reponse_data = Blog.objects.filter(publish=True).order_by('-publish_date')
    peginator = Paginator(reponse_data,2)
    page_number = request.GET.get('page',1)
    posts = peginator.get_page(page_number)
    if(request.htmx):
        return render(request, 'card2.html',{'posts':posts})
    return render(request, 'all blogs.html', {'posts': posts, 'data': get_web_data(), 'index': 'All Blogs'})

def serialize_blog(request, blog):
    return {
        'id': blog.id,
        'title': blog.title,
        'slug': blog.slug,
        'summary': blog.summary,
        'publish_date': blog.publish_date.isoformat() if blog.publish_date else None,
        'body': blog.body,
        'views': blog.views,
        'publish': blog.publish,
        'pinned': blog.pinned,
        'author_id': blog.author_id,
        'author_name': blog.author.get_full_name() or blog.author.username,
        'tags': [t.tag for t in blog.tags.all()],
        'image': request.build_absolute_uri(blog.image.url) if blog.image else None,
    }

def BlogsApi(request):
    search = request.GET.get('search', '').strip()
    reponse_data = Blog.objects.filter(publish=True).order_by('-pinned', '-publish_date')
    if search:
        reponse_data = reponse_data.filter(
            models.Q(title__icontains=search) | models.Q(summary__icontains=search)
        )
    peginator = Paginator(reponse_data, 5)
    page_number = request.GET.get('page', 1)
    posts = peginator.get_page(page_number)
    serialized_posts = [serialize_blog(request, post) for post in posts]
    response_data = {
        'data': serialized_posts,
        'has_next': posts.has_next(),
        'total_pages': peginator.num_pages,
    }
    return JsonResponse(response_data, safe=False)


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
    return render(request, 'detail.html', {'blog': blogdetails, 'data': get_web_data(), 'comments': comments, 'replyDict': replyDict, 'moreBlogs': PopularPosts})

def detailApi(request,slug):
    blogdetails = get_object_or_404(Blog, slug=slug)
    blogdetails.views = blogdetails.views + 1
    blogdetails.save()
    article_tags_ids = blogdetails.tags.values_list('pk', flat=True)
    similar_published_articles = Blog.objects.filter(tags__in=article_tags_ids)\
                                    .exclude(pk=blogdetails.pk)
    similar_articles = similar_published_articles.annotate(same_tags_in_article=Count('tags'))\
                                .order_by('-same_tags_in_article')[:2]
    serialized_blog = [serialize_blog(request, blogdetails)]
    serialized_similar = [serialize_blog(request, article) for article in similar_articles]
    data = {'data': serialized_blog, 'related': serialized_similar}
    return JsonResponse(data,safe=False)
