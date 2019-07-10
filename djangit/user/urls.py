from django.urls import path
from django.contrib import admin

from djangit.user.views import Homepage, ViewSpecificUserHomepage
from djangit.user.models import DjangitUser

admin.site.register(DjangitUser)

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    # could add u/ or user/ for users; str in urls; slug; separate endpoints
    path('user/<str:username>/', ViewSpecificUserHomepage.as_view()),
    # path('<str:subdjangit>/', ViewSpecificSubdjangit.as_view()),
]
