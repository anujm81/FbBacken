# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 12:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fbbackend', '0006_auto_20170423_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='friend',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='to_user',
        ),
        migrations.AlterUniqueTogether(
            name='friendshiprequest',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='friendshiprequest',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='friendshiprequest',
            name='to_user',
        ),
        migrations.AlterUniqueTogether(
            name='messages',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='messages',
            name='mess_from_user',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='mess_to_user',
        ),
        migrations.RemoveField(
            model_name='uploadedpics',
            name='uploaded_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.DeleteModel(
            name='FriendshipRequest',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.DeleteModel(
            name='UploadedPics',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
