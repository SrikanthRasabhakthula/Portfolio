from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("about",about,name="about"),
    path("projects",projects,name="projects"),
    path("certificates",certificates,name="certificates"),
    path("contact",contact,name="contact"),
]
