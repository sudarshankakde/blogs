from django.urls import path, include
from . import views
from blog import views as blogViews

urlpatterns = [
    # apis for extenal use
    path('Blogs',blogViews.BlogsApi, name='AllBlogsApi'),
    path('detail/<str:slug>',blogViews.detailApi, name='detailApi'),
    path('projects',views.projectsApi, name=''),
    path('newsletter',views.newsletterSubscription, name=''),
    path('contact',views.contactApi, name=''),
]
