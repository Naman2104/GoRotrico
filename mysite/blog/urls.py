from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="blogHome"),
    path("contact/",views.contact,name="contact"),
    path("blogpost/<int:id>",views.blogpost,name="blogPost")
]
