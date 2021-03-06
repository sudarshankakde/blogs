# Generated by Django 3.2.8 on 2021-12-01 05:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0035_blog_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(default=0, null=True, related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
