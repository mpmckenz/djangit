from djangit.user.models import DjangitUser
from django.shortcuts import redirect, render
from djangit.notification.models import Notification
import re
from django.views import View


class Notifications(View):
    def get(self, request):
        html = "notifications.html"
        notifications = request.user.djangit.notification_set.get_queryset().all()
        posts = []
        for check in notifications:
            if not check.noticed:
                posts += [check.post]
                Notification.objects.filter(pk=check.pk).update(noticed=True)
        return render(request, html, {'posts': posts})
