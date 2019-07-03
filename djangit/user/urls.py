from django.urls import path
from django.contrib import admin

from djangit.user.views import Index, SignUp, Login, Logout
from djangit.user.models import DjangitUser

admin.site.register(DjangitUser)

urlpatterns = [
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('signup/', SignUp.as_view()),
    path('', Index.as_view(), name='homepage'),
]
