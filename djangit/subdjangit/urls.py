from django.urls import path
from django.contrib import admin

<<<<<<< HEAD
from djangit.subdjangit.views import CreateNewSub
from djangit.subdjangit.views import SingleSubdjangit
=======
from djangit.subdjangit.views import SubdjangitList, SingleSubdjangit, CreateSubdjangit
>>>>>>> 3a9dfddb703819e4132969454634398316da5aa9
from djangit.subdjangit.models import Subdjangit

admin.site.register(Subdjangit)

urlpatterns = [
<<<<<<< HEAD
    path("subdjangits", CreateNewSub.as_view(), name="subdjangits"),
    path("<str:Subdjangit.title>/", SingleSubdjangit.as_view(), name="singlesubdjangit")

=======
    path("subdjangits/", SubdjangitList.as_view(), name="subdjangits"),
    path("createsubdjangit/", CreateSubdjangit.as_view(), name='createsubdjangit'),
    path("r/<slug:title>/", SingleSubdjangit.as_view(), name="singlesubdjangit")
>>>>>>> 3a9dfddb703819e4132969454634398316da5aa9
]
