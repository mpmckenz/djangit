from django.urls import path
from django.contrib import admin

from djangit.subdjangit.views import SubdjangitList, SingleSubdjangit, CreateSubdjangit, DeleteSubdjangit
from djangit.subdjangit.models import Subdjangit

admin.site.register(Subdjangit)

urlpatterns = [
    path("subdjangits/", SubdjangitList.as_view(), name="subdjangits"),
    path("createsubdjangit/", CreateSubdjangit.as_view(), name='createsubdjangit'),
    path("r/<slug:title>/", SingleSubdjangit.as_view(), name="singlesubdjangit"),
    path('deletesubdjangit/', DeleteSubdjangit.as_view(), name='deletesubdjangit'),
]
