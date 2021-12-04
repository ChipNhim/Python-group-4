from django.urls import path
from workcalendar import views
urlpatterns = [
    path("", views.user_login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.user_logout, name="logout"),
    path("car/list_car/", views.list_car, name="list_car"),
    path("room/list_room/", views.list_room, name="list_room"),
    path("dashboard/calendar", views.list_calendar, name="calendar"),
    path("car/create_car/", views.create_car, name="create_car"),
    path("car/edit_car/<int:pk>", views.edit_car, name="edit_car"),
    path("car/approve_car/", views.approve_car, name="approve_car"),
    path("car/approve/<int:pk>", views.approve, name="approve"),
    path("car/delete_car/<int:pk>", views.delete_car, name="delete_car"),
    path("dashboard/creat_calendar", views.creat_calendar, name = "creat_calendar"),
    path("car/show_car/<int:pk>", views.show_car, name = "show_car")
]
