from django.urls import path
from django.contrib import admin

from djangit.subdjangit.views import CreateNewSub
from djangit.subdjangit.views import SingleSubdjangit
from djangit.subdjangit.models import Subdjangit

admin.site.register(Subdjangit)

urlpatterns = [
    path("subdjangits", CreateNewSub.as_view(), name="subdjangits"),
    path("<str:Subdjangit.title>/", SingleSubdjangit.as_view(), name="singlesubdjangit")

]
