from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth  import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

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

def list_approve(request):
    rooms = Room.objects.filter(room_type=0)
    query_params = request.GET
    date_from = query_params.get("date_from", None)
    date_to = query_params.get("date_to", None)
    phong1 = query_params.get("phong1", None)
    print(query_params)
    # Lay lich xe da duoc duyet
    cars = Vehicle.objects.filter(check=1)
    if date_from is not None:
        cars = cars.filter(date_start__gte=date_from)  # greater than equal
    if date_to is not None:
        cars = cars.filter(date_start__lte=date_to)
    if phong1 is not None and phong1:
        cars = cars.filter(room=phong1)

    return render(request, "car/list_approve.html", {"cars": cars, "rooms": rooms})

def list_car(request):
    cars = Vehicle.objects.filter(check=0,room_id =request.user.room_id)
    return render(request, "car/list_car.html", {"cars": cars})
def list_room(request):
    calendar_data_WC = Workcalendar.objects.filter(room_id=1)
    return render(request, "calendar/list_calendar.html",{"calendar_data_WC": calendar_data_WC})

@login_required
def create_car(request):
    if request.method=="GET":
        # rooms = Room.objects.filter()
        return render(request, "car/create_car.html")
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
    query_params = request.GET
    date_from_approve = query_params.get("date_from_approve", None)
    date_to_approve = query_params.get("date_to_approve", None)
    # Lay het lich xe tu ngay den ngay da chon
    cars = Vehicle.objects.filter(check=0)
    if date_from_approve is not None:
        cars = cars.filter(date_start__gte=date_from_approve)  # greater than equal
    if date_to_approve is not None:
        cars = cars.filter(date_start__lte=date_to_approve)
    return render(request, "car/approve_car.html", {"cars": cars})

@permission_required("workcalendar.can_approve_car")
def approve(request, pk):
    cars = get_object_or_404(Vehicle, pk=pk)
    vetypes = Vehicle.VE_TYPE
    if request.method =="POST":
        data = request.POST
        cars.date_start = data.get("datestart")
        cars.date_end = data.get("dateend")
        cars.ve_type = data.get("loaixe","") 
        cars.check = 1
        cars.save()
        return redirect("approve_car") 
    return render(request, "car/approve.html", {"cars": cars, "vetypes": vetypes})

def show_car(request, pk):
    cars = Vehicle.objects.get(id=pk)
    return render(request, "car/show_car.html", {"cars": cars}) 
   
def delete_car(request, pk):
    car= get_object_or_404(Vehicle, pk=pk)
    car.delete()
    return redirect("approve_car")

def edit_car(request, pk):
    cars = get_object_or_404(Vehicle, pk=pk)
    if request.method =="POST":
        data = request.POST
        cars.plan = data.get("plan","")
        cars.date_start = data.get("datestart","")
        cars.date_end = data.get("dateend","")
        cars.descript = data.get("descript","")
        cars.team_leader = data.get("leader","")
        cars.phone_number = data.get("phone","")
        cars.num_mem = data.get("number","")
        cars.loc_start = data.get("locstart","")
        cars.loc_end = data.get("locend","")
        cars.distance = data.get("distance","") 
        cars.save()  
    return render(request, "car/edit_car.html", {"cars": cars})   

def list_calendar(request, method = "GET"):
    calendar_data_WC = Workcalendar.objects.filter(cal_check = 1)
    return render(request, "calendar/list_calendar.html",{"calendar_data_WC": calendar_data_WC})

def approve_calendar(request, method = "GET"):
    ap_workcalendar = Workcalendar.objects.filter(cal_check = 0)
    return render(request, "calendar/approve_calendar.html",{"ap_workcalendar": ap_workcalendar})

def creat_calendar(request):
    if request.method == "GET": 
        workcalendar = Workcalendar.objects.all()
        rooms = Room.objects.all()
        return render(request, "calendar/creat_calendar.html", {"workcalendar": workcalendar, "rooms": rooms})
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

def show_workcalendar(request, pk):
    workcalendar = Workcalendar.objects.get(id=pk)
    return render(request, "calendar/show_workcalendar.html", {"workcalendar": workcalendar}) 

def edit_calendar(request, pk):
    edit_workcalendar = get_object_or_404(Workcalendar, pk = pk)
    if request.method == "GET":
        edit_room = Room.objects.all()
        return render(request, "calendar/edit_calendar.html", 
            {"edit_workcalendar": edit_workcalendar, "edit_room": edit_room})
    elif request.method == "POST":
        data = request.POST
        edit_workcalendar.worktime_from = data.get("worktime_from", "")
        edit_workcalendar.worktime_to = data.get("worktime_to", "")
        edit_workcalendar.Room = data.get("Room", "")
        edit_workcalendar.descript = data.get("descript", "")
        edit_workcalendar.pic = data.get("pic", "")
        edit_workcalendar.member = data.get("member", "")
        edit_workcalendar.service = data.get("service", "")
        edit_workcalendar.assign = data.get("assign", "")
        edit_workcalendar.save()
        return redirect('approve_calendar')

def delete_calendar(request, pk):
    workcalendar = get_object_or_404(Workcalendar, pk=pk)
    workcalendar.delete()
    return redirect('approve_calendar')

def approve_approve_calendar(request, pk):
    workcalendar = get_object_or_404(Workcalendar, pk=pk)
    workcalendar.cal_check = 1
    workcalendar.save()
    return redirect('approve_calendar')

def stop_calendar(request, pk):
    workcalendar = get_object_or_404(Workcalendar, pk=pk)
    workcalendar.cal_check = 0
    workcalendar.save()
    return redirect('calendar')

def pre_edit_calendar(request, method = "GET"):
    workcalendar = Workcalendar.objects.filter(cal_check = 0)
    return render(request, "calendar/pre_edit_calendar.html",{"workcalendar": workcalendar})

def edit_pre_edit_calendar(request, pk):
    edit_workcalendar = get_object_or_404(Workcalendar, pk = pk)
    if request.method == "GET":
        edit_room = Room.objects.all()
        return render(request, "calendar/edit_pre_edit_calendar.html", 
            {"edit_workcalendar": edit_workcalendar, "edit_room": edit_room})
    elif request.method == "POST":
        data = request.POST
        edit_workcalendar.worktime_from = data.get("worktime_from", "")
        edit_workcalendar.worktime_to = data.get("worktime_to", "")
        edit_workcalendar.Room = data.get("Room", "")
        edit_workcalendar.descript = data.get("descript", "")
        edit_workcalendar.pic = data.get("pic", "")
        edit_workcalendar.member = data.get("member", "")
        edit_workcalendar.service = data.get("service", "")
        edit_workcalendar.assign = data.get("assign", "")
        edit_workcalendar.save()
        return redirect('pre_edit_pre_calendar')

def delete_pre_edit_calendar(request, pk):
    workcalendar = get_object_or_404(Workcalendar, pk=pk)
    workcalendar.delete()
    return redirect('pre_edit_calendar')

@login_required
def userprofile(request, pk):
    users = get_object_or_404(MyUser, pk=pk)
    
    print("========================")
    print(request.method)

    if request.method == "POST":
        data = request.POST
        users.Fname = data.get("Fullname", "")
        # users.room.name = data.get("room", "")
        # user.author = form.cleaned_data["author"]
        # user.published_date = form.cleaned_data["published_date"]
        users.save()
        messages.success(request, "Update profile successful")
        return redirect('dashboard')
        # return HttpResponseRedirect("dashboard/")
    return render(request, "dashboard/userprofile.html", {"users" : users})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            # messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        # else:
            # messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/change_password.html', {'form': form})