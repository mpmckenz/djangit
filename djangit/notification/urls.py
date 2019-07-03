from django.urls import path
from djangit.notification.models import Notification
from djangit.notification.views import Notifications
from django.contrib import admin

admin.site.register(Notification)


urlpatterns = [
    path("notifications/", Notifications.as_view())
]
