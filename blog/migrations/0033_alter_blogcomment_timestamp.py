# Generated by Django 3.2.8 on 2021-11-29 17:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_alter_blogcomment_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='timeStamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
