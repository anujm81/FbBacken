# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 19:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_unused_friend_relation', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=4000)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('mess_from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_from_user', to=settings.AUTH_USER_MODEL)),
                ('mess_to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='images/')),
                ('cover_pic', models.ImageField(upload_to='images/')),
                ('about', models.CharField(blank=True, max_length=4000, null=True)),
                ('intro', models.CharField(blank=True, max_length=4000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedPics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(blank=True, max_length=4000, null=True)),
                ('Upload_image', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='messages',
            unique_together=set([('mess_from_user', 'mess_to_user')]),
        ),
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
