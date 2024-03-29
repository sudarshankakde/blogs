# Generated by Django 4.0.2 on 2022-07-18 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_auto_20211201_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=25)),
                ('Email_Id', models.EmailField(max_length=254)),
                ('Message_To_Me', models.TextField()),
                ('Contacted_On', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
