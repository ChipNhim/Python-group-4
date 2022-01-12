from django.urls import path
from workcalendar import views
urlpatterns = [
    path("", views.user_login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.user_logout, name="logout"),
    path("dashboard/userprofile/<int:pk>", views.userprofile, name="userprofile"),
    path("dashboard/change_password/", views.change_password, name="change_password"),
    path("car/list_car/", views.list_car, name="list_car"),
    path("car/list_approve/", views.list_approve, name="list_approve"),
    path("room/list_room/", views.list_room, name="list_room"),
    path("dashboard/list_calendar", views.list_calendar, name="list_calendar"),
    path("car/create_car/", views.create_car, name="create_car"),
    path("car/edit_car/<int:pk>", views.edit_car, name="edit_car"),
    path("car/approve_car/", views.approve_car, name="approve_car"),
    path("car/approve/<int:pk>", views.approve, name="approve"),
    path("car/delete_car/<int:pk>", views.delete_car, name="delete_car"),
    path("dashboard/creat_calendar", views.creat_calendar, name = "creat_calendar"),
    path("car/show_car/<int:pk>", views.show_car, name = "show_car"),
    path("calendar/show_workcalendar/<int:pk>", views.show_workcalendar, name = "show_workcalendar"),
    path("dashboard/approve_calendar", views.approve_calendar, name = "approve_calendar"),
    path("dashboard/edit_calendar/<int:pk>", views.edit_calendar, name = "edit_calendar"),
    path("dashboard/approve_approve_calendar/<int:pk>", views.approve_approve_calendar, name = "approve_approve_calendar"),
    path("dashboard/delete_calendar/<int:pk>", views.delete_calendar, name = "delete_calendar"),
    path("dashboard/stop_calendar/<int:pk>", views.stop_calendar, name = "stop_calendar"),
    path("dashboard/pre_edit_calendar", views.pre_edit_calendar, name = "pre_edit_calendar"),
    path("dashboard/edit_pre_edit_calendar/<int:pk>", views.edit_pre_edit_calendar, name = "edit_pre_edit_calendar"),
    path("dashboard/delete_pre_calendar/<int:pk>", views.delete_pre_edit_calendar, name = "delete_pre_edit_calendar")
]
