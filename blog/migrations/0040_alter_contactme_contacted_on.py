# Generated by Django 4.0.2 on 2022-07-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_contactme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='Contacted_On',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]
