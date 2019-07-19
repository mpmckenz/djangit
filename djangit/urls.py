"""djangit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404, handler500
from djangit.user.urls import urlpatterns as user_urls
from djangit.post.urls import urlpatterns as post_urls
from djangit.authentication.urls import urlpatterns as authentication_urls
from djangit.subdjangit.urls import urlpatterns as subdjangit_urls
import djangit


handler404 = djangit.authentication.views.handler404
handler500 = djangit.authentication.views.handler500
handler404 = djangit.post.views.handler404
handler500 = djangit.post.views.handler500
handler404 = djangit.subdjangit.views.handler404
handler500 = djangit.subdjangit.views.handler500
handler404 = djangit.user.views.handler404
handler500 = djangit.user.views.handler500


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += authentication_urls
urlpatterns += post_urls
urlpatterns += user_urls
urlpatterns += subdjangit_urls
