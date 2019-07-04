from django.urls import path
from django.contrib import admin

from djangit.subdjangit.views import SubdjangitList
from djangit.subdjangit.models import Subdjangit

admin.site.register(Subdjangit)

urlpatterns = [
    path('subdjangits', SubdjangitList.as_view(), name='subdjangits'),
]
