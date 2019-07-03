from django.contrib import admin
from django.urls import path
from djangit.authentication.views import SignUp, Login, Logout

# MM: when a user signs out the url paths FOR SOME REASON
#  adds 'accounts/' before login url so I included that so
#  the page could land. IF FIXED: correct signupform.html a tag

urlpatterns = [
    path("accounts/login/", Login.as_view()),
    path('signup/', SignUp.as_view()),
    path("logout/", Logout.as_view()),
]
