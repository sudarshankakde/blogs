# Generated by Django 3.2.8 on 2021-11-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
