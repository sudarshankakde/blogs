# Generated by Django 3.2.8 on 2021-11-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_webdata_homepage_slide_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimages',
            name='img',
            field=models.ImageField(null=True, upload_to='images/homepage/'),
        ),
    ]