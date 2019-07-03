from django.urls import path
from django.contrib import admin

from djangit.user.views import Profile
from djangit.user.models import DjangitUser

admin.site.register(DjangitUser)

urlpatterns = [
    path('', Profile.as_view(), name='homepage'),
]
