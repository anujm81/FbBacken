# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from fbbackend.models import UploadedPics, Friend, FriendshipRequest, Messages, Comments
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(UploadedPics)
admin.site.register(Friend)
admin.site.register(FriendshipRequest)
admin.site.register(Messages)
admin.site.register(Comments)
