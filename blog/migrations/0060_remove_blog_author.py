# Generated by Django 4.0.2 on 2022-09-10 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0059_alter_blog_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]
