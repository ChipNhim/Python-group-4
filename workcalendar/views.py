from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth  import logout
from django.contrib.auth.decorators import login_required

from .models import Vehicle, Room, Workcalendar, MyUser, MyUserManager
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
def list_room(request):
    calendar_data_WC = Workcalendar.objects.filter(room_id=1)
    return render(request, "calendar/list_calendar.html",{"calendar_data_WC": calendar_data_WC})

def list_calendar(request, method = "GET"):
    calendar_data_WC = Workcalendar.objects.filter(cal_check = 1)
    return render(request, "calendar/list_calendar.html",{"calendar_data_WC": calendar_data_WC})

def create_car(request):
    if request.method=="GET":
        rooms = Room.objects.filter(room_type=0)
        return render(request, "car/create_car.html", context={"rooms": rooms})
    elif request.method=="POST":
        data = request.POST
        plan = data.get("plan","")
        room = int(data.get("phong", None))
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
        num_mem=num_mem,loc_start=loc_start,loc_end=loc_end,distance=distance,check=0)
        create_car.save()
        # messages.success(request, "Dang ky thanh cong")
        return redirect("list_car")

def approve_car(request):
    cars = Vehicle.objects.all
    return render(request, "car/approve_car.html", {"cars": cars})

def approve(request, pk):
    cars = get_object_or_404(Vehicle, pk=pk)
    vetypes = Vehicle.VE_TYPE
    if request.method =="POST":
        data = request.POST
        cars.date_start = data.get("datestart")
        cars.date_end = data.get("dateend")
        cars.descript = data.get("descript","")
        cars.team_leader = data.get("leader","")
        cars.loc_start = data.get("locstart","")
        cars.loc_end = data.get("locend","")
        cars.ve_type = data.get("loaixe","") 
        cars.check = 1
        # approve=Vehicle(date_start=date_start,date_end=date_end,
        # descript=descript,team_leader=team_leader,loc_start=loc_start,loc_end=loc_end,
        # ve_type=ve_type,check=1)
        cars.save()
        return redirect("approve_car") 
    return render(request, "car/approve.html", {"cars": cars, "vetypes": vetypes})
   
def delete_car(request, pk):
    car= get_object_or_404(Vehicle, pk=pk)
    car.delete()

def edit_car(request, pk):
    cars = get_object_or_404(Vehicle, pk=pk)
    if request.method =="POST":
        data = request.POST
        cars.plan = data.get("plan","")
        cars.room = int(data.get("phong", None))
        date_start = data.get("datestart","")
        date_end = data.get("dateend","")
        descript = data.get("descript","")
        team_leader = data.get("leader","")
        phone_number = data.get("phone","")
        num_mem = data.get("number","")
        loc_start = data.get("locstart","")
        loc_end = data.get("locend","")
        distance = data.get("distance","")   
    return render(request, "car/edit_car.html", {"cars": cars})   

def creat_calendar(request):
    if request.method == "GET": 
        workcalendars = Workcalendar.objects.all()
        rooms = Room.objects.all()
        return render(request, "calendar/creat_calendar.html", {"workcalendars": workcalendars, "rooms": rooms})
    elif request.method  == "POST":
        data = request.POST
        worktime_from = data.get("worktime_from", "")
        worktime_to = data.get("worktime_to", "")
        room = data.get("room", "")
        descript = data.get("descript", "")
        pic = data.get("pic", "")
        member = data.get("member","")
        service = data.get("service", "")
        assign = data.get("assign", "")
        workcalendar = Workcalendar(worktime_from = worktime_from, worktime_to = worktime_to,
            room_id = room, descript = descript, pic = pic, member = member, service = service, 
            assign = assign, cal_check = 0)
        workcalendar.save()
        return redirect("calendar")

def show_car(request, pk):
    cars = Vehicle.objects.get(id=pk)
    return render(request, "car/show_car.html", {"cars": cars}) 
# def approve_calendar(request, pk):
#     workcalendars = get_object_or_404(Workcalendar, pk = pk)
#     if request.method == "POST"
#         data = request.POST
#         workcalendars.worktime_from = data.("worktime_from", "")
#         workcalendars.worktime_to = data.("worktime_to", "")
#         workcalendars.room = data.("room", "")
#         workcalendars.descript = data.("descript", "")
#         workcalendars.pic = data.("pic", "")
#         workcalendars.member = data.("member", "")
#         workcalendars.service = data.("service", "")




def show_workcalendar(request, pk):
    workcalendar = Workcalendar.objects.get(id=pk)
    return render(request, "calendar/show_workcalendar.html", {"workcalendar": workcalendar}) 

def approve_calendar(request, pk):
    workcalendars = get_object_or_404(Workcalendar, pk = pk)
    if request.method == "POST":
        data = request.POST
        workcalendars.worktime_from = data.get("worktime_from", "")
        workcalendars.worktime_to = data.get("worktime_to", "")
        workcalendars.room = data.get("room", "")
        workcalendars.descript = data.get("descript", "")
        workcalendars.pic = data.get("pic", "")
        workcalendars.member = data.get("member", "")
        workcalendars.service = data.get("service", "")
        workcalendars.assign = data.get("assign", "")
    return render(request, "calendar/approve_calendar.html",{"workcalendars": workcalendars})
