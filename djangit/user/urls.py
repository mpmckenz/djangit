from django.urls import path
from django.contrib import admin

from djangit.user.views import Homepage
from djangit.user.models import DjangitUser

admin.site.register(DjangitUser)

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
]
