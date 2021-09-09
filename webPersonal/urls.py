from os import name
import django
from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views
from django.conf import settings

urlpatterns = [
    path ("", core_views.home,name= "home"),
    path("about/",core_views.about,name= "about"),
    path("portfolio/",portfolio_views.portfolio, name="portfolio"),
    path('contact/', core_views.contact, name="contact"),
    path('admin/', admin.site.urls),
]

