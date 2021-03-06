# Generated by Django 2.1 on 2018-09-20 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theSink', '0008_auto_20180919_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='Message', verbose_name=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('used', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userMessages', to='theSink.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='message_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='theSink.Message'),
        ),
    ]
