from django.urls import path
from django.contrib import admin

from djangit.user.views import Homepage, ViewSpecificUserHomepage, AllUsers, ToggleSubscription, DeletePost, DeleteSubdjangit
from djangit.user.models import DjangitUser

admin.site.register(DjangitUser)

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    # could add u/ or user/ for users; str in urls; slug; separate endpoints
    path('user/<str:username>/', ViewSpecificUserHomepage.as_view()),
    # path('<str:subdjangit>/', ViewSpecificSubdjangit.as_view()),
    path('allusers/', AllUsers.as_view(), name='allusers'),
    path("subscribe/<str:url>/", ToggleSubscription.as_view()),
    path('deletepost/<int:id>/<str:url>/',
         DeletePost.as_view(), name='deletepost'),
    path('deletesubdjangit/', DeleteSubdjangit.as_view(), name='deletesubdjangit'),

]
