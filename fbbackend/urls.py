from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^allFriends/$', views.getAllFrnds, name='allFriends'),
    url(r'^allMsgs/$', views.getAllMsgs, name='allMsgs'),
    url(r'^allRequests/$', views.getAllFrndRequest, name='allRequest'),
    url(r'^allComments/$', views.getAllComments, name='allComments'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)