from django.urls import path, include
from . import views
from blog import views as blogViews
from blog import deploy

urlpatterns = [
    # apis for extenal use
    path('blogs',blogViews.BlogsApi, name='AllBlogsApi'),
    path('detail/<str:slug>',blogViews.detailApi, name='detailApi'),
    path('projects',views.projectsApi, name=''),
    path('projects/detail/<str:slug>', views.projectDetailApi, name='projectDetailApi'),

    path('newsletter',views.newsletterSubscription, name=''),
    path('contact',views.contactApi, name=''),
    path('stack',views.stackApi, name=''),
    path('deploy-webhook', deploy.deploy_webhook, name='deploy_webhook'),
    path('resume', views.resumeApi, name='resumeApi'),
    path('experience', views.experienceApi, name='experienceApi'),
    path('gallery', views.galleryApi, name='galleryApi'),
    path('about', views.aboutApi, name='aboutApi'),
]


