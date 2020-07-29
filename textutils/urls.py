"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

# code of video 6

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='Index'),
#     path('about/', views.about, name='about'),
#     path('file/', views.existingFile, name='file'),
#     path('navigation/', views.navigator, name='navigator')
# ]

# code for video-9
# urlpatterns = [
#      path('admin/', admin.site.urls),
#      path('', views.index, name='Index'),
#      path('removepunctuation/', views.removepunctuation, name='removepunctuation'),
#      path('capitalizefirst/', views.capitalizefirst, name='capitalizefirst'),
#      path('newlineremove/', views.newlineremove, name='newlineremove'),
#      path('spaceremover/', views.spaceremover, name='spaceremover'),
#      path('charcount/', views.charcount, name='charcount'),
# ]

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.index, name='Index'),
     path('analyse/', views.analyse, name='analyse'),
]