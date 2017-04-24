# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fbbackend', '0009_auto_20170423_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_from_user', to='fbbackend.UserProfile'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_unused_friend_relation', to='fbbackend.UserProfile'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='fbbackend.UserProfile'),
        ),
        migrations.AlterField(
            model_name='friendshiprequest',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_requests_sent', to='fbbackend.UserProfile'),
        ),
        migrations.AlterField(
            model_name='friendshiprequest',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_requests_received', to='fbbackend.UserProfile'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='mess_from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_from_user', to='fbbackend.UserProfile'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='mess_to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_to_user', to='fbbackend.UserProfile'),
        ),
    ]