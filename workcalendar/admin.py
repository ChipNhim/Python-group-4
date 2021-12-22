
from django.contrib import admin
from .models import MyUser

from .models import Room, Workcalendar, Vehicle
from .models import MyUser

# Register your models here.
admin.site.register(Room)
admin.site.register(Workcalendar)
admin.site.register(Vehicle)
admin.site.register(MyUser)