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
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


from django.views.static import serve


admin.site.site_header = "Sid's Blogs"
admin.site.site_title = "Sid's Admin Panel"
admin.site.index_title = "Welcome to Sid's Admin Panel"

urlpatterns = [
    # admin panel
    path('AdminPanel/', admin.site.urls),


    # contact page
    path('contact', views.contact, name='contact'),

    path('aboutme', views.aboutme, name='aboutme'),



    # search in blogs
    path('search', views.search, name='search'),

    # user login , singup , logout
    path('singup', views.handleSingup, name='singup'),
    path('checkForUserName', views.checkForUserName, name='checkForUserName'),
    path('checkForUserMail', views.checkForUserMail, name='checkForUserMail'),
    # login
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handelLogout, name="handleLogout"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('reset_password', auth_views.PasswordResetView.as_view(
        template_name='Extra/Reset_Email_card.html'), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(
        template_name='Extra/Reset_Email_Sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='Extra/Reset_password_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='Extra/Reset_password_done.html'), name='password_reset_complete'),



    # privacy_policy
    path('Privacy_Policy', views.Privacy_Policy, name='Privacy_Policy'),
    # blog post comment
    path('postComment', views.postComment, name='postComment'),

    # email updates newsletter
    path('newsletter', views.newsletter, name='newsletter'),

    # home page
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('subscription', views.subscription, name='subscription'),


    #blogs and etc
    path('AllBlogs', views.AllBlogs, name='AllBlogs'),

    #blogs in detail
    path('<str:slug>', views.detail, name='detail'),

    path('GetMoreBlog/<int:number>', views.GetMoreBlog, name='GetMoreBlog'),
    re_path(r'^DataBase/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),

    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),

]

handler404 = 'sid.views.error_404_view'
handler500 = 'sid.views.handler500'
