# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.core.exceptions import ValidationError
from django.core.files import images
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from friendship.signals import (
    friendship_request_created, friendship_request_rejected,
    friendship_request_canceled,
    friendship_request_viewed, friendship_request_accepted,)

from django.conf import settings

from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='images/')
    cover_pic= models.ImageField(upload_to='images/')
    about = models.CharField(max_length=4000, blank=True, null=True)
    intro = models.CharField(max_length=4000, blank=True, null=True)




class UploadedPics(models.Model):
    caption = models.CharField(max_length=4000, blank=True, null=True)
    Upload_image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='uploaded_by' )



class Friend(models.Model):
    """ Model to represent Friendships """
    to_user = models.ForeignKey(User, related_name='friends')
    from_user = models.ForeignKey(User, related_name='_unused_friend_relation')
    created = models.DateTimeField(default=timezone.now)


    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return "User #%s is friends with #%s" % (self.to_user_id, self.from_user_id)

    def save(self, *args, **kwargs):
        # Ensure users can't be friends with themselves
        if self.to_user == self.from_user:
            raise ValidationError("Users cannot be friends with themselves.")
        super(Friend, self).save(*args, **kwargs)

class FriendshipRequest(models.Model):
    """ Model to represent friendship requests """
    from_user = models.ForeignKey(UserProfile, related_name='friendship_requests_sent')
    to_user = models.ForeignKey(UserProfile, related_name='friendship_requests_received')

    message = models.TextField(_('Message'), blank=True)

    created = models.DateTimeField(default=timezone.now)
    rejected = models.DateTimeField(blank=True, null=True)
    viewed = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _('Friendship Request')
        verbose_name_plural = _('Friendship Requests')
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return "User #%s friendship requested #%s" % (self.from_user_id, self.to_user_id)

    def accept(self):
        """ Accept this friendship request """
        relation1 = Friend.objects.create(
            from_user=self.from_user,
            to_user=self.to_user
        )

        relation2 = Friend.objects.create(
            from_user=self.to_user,
            to_user=self.from_user
        )

        friendship_request_accepted.send(
            sender=self,
            from_user=self.from_user,
            to_user=self.to_user
        )

        self.delete()

        # Delete any reverse requests
        FriendshipRequest.objects.filter(
            from_user=self.to_user,
            to_user=self.from_user
        ).delete()



        return True

    def reject(self):
        """ reject this friendship request """
        self.rejected = timezone.now()
        self.save()
        friendship_request_rejected.send(sender=self)

    def cancel(self):
        """ cancel this friendship request """
        self.delete()
        friendship_request_canceled.send(sender=self)

        return True

    def mark_viewed(self):
        self.viewed = timezone.now()
        friendship_request_viewed.send(sender=self)
        self.save()
        return True

class Messages(models.Model):
    """ Model to represent Messages"""
    mess_to_user = models.ForeignKey(UserProfile, related_name='message_to_user')
    mess_from_user = models.ForeignKey(UserProfile, related_name='message_from_user')
    message = models.CharField(max_length=4000, blank=False, null=False)
    created = models.DateTimeField(default=timezone.now)

    class Meta:

        unique_together = ('mess_from_user', 'mess_to_user'),

class Comments(models.Model):
    """Model to represent Comments on the uploaded posts"""
    post = models.ForeignKey(UploadedPics,on_delete=models.CASCADE, related_name='post')
    comment = models.CharField(max_length=4000, blank=False, null=False)
    from_user = models.ForeignKey(UserProfile, related_name='comment_from_user')
    created = models.DateTimeField(default=timezone.now)

