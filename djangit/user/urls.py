from django.urls import path
from django.contrib import admin

from djangit.user.views import Index
from djangit.user.models import DjangitUser

admin.site.register(DjangitUser)

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
]