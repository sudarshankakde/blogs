# Generated by Django 3.2.8 on 2021-11-28 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_sliderimages_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webdata',
            name='Homepage_slide_imgs',
        ),
        migrations.AddField(
            model_name='webdata',
            name='my_image',
            field=models.ImageField(default=1, upload_to='images/homepage'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='sliderImages',
        ),
    ]
