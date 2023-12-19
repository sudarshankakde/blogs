from django.urls import path, include
from . import views
app_name  = 'blog'
urlpatterns = [
     #blogs and etc
    path('', views.AllBlogs, name='AllBlogs'),

    #blogs in detail
    path('<str:slug>', views.detail, name='detail'),


]
