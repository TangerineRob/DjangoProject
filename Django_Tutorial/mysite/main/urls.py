from django.urls import path

from . import views

urlpatterns = [
path("", views.index, name="index"),
path("views/", views.views, name="view 1"),
path("sign_in/", views.sign_in, name="Sign_In"),
]

