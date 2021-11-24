from django.urls import path
from workcalendar import views
urlpatterns = [
    path("", views.user_login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.user_logout, name="logout"),
    path("car/list_car/", views.list_car, name="list_car"),
    path("dashboard/calendar", views.list_calendar, name="calendar"),
    path("dashboard/creat_calendar", views.creat_calendar, name = "creat_calendar")
]