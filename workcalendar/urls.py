from django.urls import path
from workcalendar import views
urlpatterns = [
    path("", views.user_login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.user_logout, name="logout"),
    path("car/list_car/", views.list_car, name="list_car"),
    path("dashboard/calendar", views.list_calendar, name="calendar"),
    path("car/create_car/", views.create_car, name="create_car"),
    path("car/approve_car/", views.approve_car, name="approve_car"),
]