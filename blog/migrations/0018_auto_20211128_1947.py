# Generated by Django 3.2.8 on 2021-11-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20211128_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='sliderImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='images/homepage/')),
            ],
        ),
        migrations.AddField(
            model_name='webdata',
            name='Homepage_slide_imgs',
            field=models.ManyToManyField(null=True, to='blog.sliderImages'),
        ),
    ]
