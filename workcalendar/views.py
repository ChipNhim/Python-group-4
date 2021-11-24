from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth  import logout
from django.contrib.auth.decorators import login_required

from .models import Vehicle
from .models import Room
from .models import Workcalendar
from .models import MyUser
from .models import MyUserManager

# Create your views here.
def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        user = authenticate(email = email, password = password)

        if user is None:
            my_message = (
                "Your email address or password is incorrect, Pleasure login again!"
            )
            messages.error(request, my_message)
            return render(request, "layouts/login.html")

        #Luu lai cac section de sau khi dang nhap vao lan dau tien ma mo cac tab, trang khac se van su dung quyen cua tai khoan user
        login(request, user) 
        return HttpResponseRedirect("dashboard/")
    return render(request, "layouts/login.html")
@login_required
def dashboard(request):
    return render(request, "dashboard/index.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
def list_car(request):
    cars = Vehicle.objects.all
    return render(request, "car/list_car.html", {"cars": cars})

def list_calendar(request, method = "GET"):
    calendar_data_WC = Workcalendar.objects.all
    return render(request, "calendar/list_calendar.html",{"calendar_data_WC": calendar_data_WC})

def create_car(request):
    if request.method=="GET":
        return render(request, "room/create_car")
    elif request.method=="POST":
        data = request.POST
        plan = data.get("plan","")
        room = data.get("room","")
        date_start = data.get("datestart","")
        date_end = data.get("dateend","")
        descript = data.get("descript","")
        team_leader = data.get("leader","")
        phone_number = data.get("phone","")
        num_mem = data.get("number","")
        loc_start = data.get("locstart","")
        loc_end = data.get("locend","")
        distance = data.get("distance","")
            
        create_car=Vehicle(plan=plan,room_id=room,date_start=date_start,date_end=date_end,
        descript=descript,team_leader=team_leader,phone_number=phone_number,
        num_mem=num_mem,loc_start=loc_start,loc_end=loc_end,distance=distance)
        create_car.save()
        return render(request, "room/create_car")
            
