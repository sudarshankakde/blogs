# Generated by Django 4.0.2 on 2022-09-04 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0046_projects_alter_blog_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]