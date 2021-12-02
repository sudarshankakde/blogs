"""sid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


admin.site.site_header = "Sid's Blogs"
admin.site.site_title = "Sid's Admin Panel"
admin.site.index_title = "Welcome to Sid's Admin Panel"

urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls),


    #contact page
    path('contact', views.contact, name='contact'),


    # search in blogs
    path('search', views.search, name='search'),

    #user login , singup , logout
    path('singup', views.handleSingup, name='singup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handelLogout, name="handleLogout"),

    #blog post comment
    path('postComment', views.postComment, name='postComment'),
    
    # email updates newsletter
    path('newsletter', views.newsletter, name='Newsletter'),
    
    # home page
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('Home', views.home, name='home'),

    #blogs and etc
    path('AllBlogs', views.AllBlogs, name='AllBlogs'),

    #blogs in detail
    path('<str:slug>', views.detail, name='detail'),

    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
