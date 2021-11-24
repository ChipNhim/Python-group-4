from django.urls import path
from workcalendar import views
urlpatterns = [
    path("", views.user_login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.user_logout, name="logout"),
    path("car/list_car/", views.list_car, name="list_car"),
]