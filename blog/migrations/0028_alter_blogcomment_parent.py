# Generated by Django 3.2.8 on 2021-11-29 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_alter_blogcomment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogcomment'),
        ),
    ]