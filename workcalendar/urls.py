from django.urls import path

from workcalendar import views

urlpatterns = [
    path("login/", views.login, name="login"),
] 
