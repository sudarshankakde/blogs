# Generated by Django 4.0.2 on 2022-09-04 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0048_tag_created_on_webdata_socail_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webdata',
            old_name='socail_link',
            new_name='Socail',
        ),
    ]
