# Generated by Django 2.1 on 2018-09-20 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theSink', '0010_auto_20180919_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
