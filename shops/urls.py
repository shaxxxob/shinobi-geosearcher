
from django.contrib import admin
from django.urls import path
from nearbyshops import views

urlpatterns = [path("admin/", admin.site.urls), path("", views.Home.as_view())]
