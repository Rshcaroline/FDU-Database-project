from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect


from .models import appoint_acm, appoint_lecture, appoint_station, Acm, Station, Lecture
from register.models import User
from .forms import AppointAcmForm, AppointLectureForm, AppointStationForm

# Create your views here.

def get_Acm(request):
    ctx = {
        'acm': Acm.objects.all()
    }
    return render(request, 'appointment/acm-list.html', ctx)

def get_Acm_detail(request, acm_id):
    name = request.session.get('username','')
    #name = response.get_cookie('username')
    try:
        acm = Acm.objects.get(id=acm_id)
    except Acm.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        #form = AppointAcmForm()
        form = AppointAcmForm(
            initial={'name': name}
        )
        #form.name = name
        #appoint_acm.name = name
        #request.session['appoint_acm.user_id'] = User_id
    else:
        form = AppointAcmForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['acm'] = acm
            appoint_acm.objects.create(**cleaned_data)

    ctx = {
        'acm': acm,
        'appoint': appoint_acm,
        'form': form,
    }

    #response = HttpResponse('appointment/acm-detail.html')
    #response.set_cookie("User.username", appoint_acm.name)
    #if "username" in request.COOKIES:
        #appoint_acm.name = request.COOKIES["username"]

    return render(request, 'appointment/acm-detail.html', ctx)

def get_Lecture(request):
    ctx = {
        'lecture': Lecture.objects.all()
    }
    return render(request, 'appointment/lecture-list.html', ctx)

def get_Lecture_detail(request, lecture_id):
    name = request.session.get('username','')
    try:
        lecture = Lecture.objects.get(id=lecture_id)
    except Lecture.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = AppointLectureForm(
            initial={'name': name}
        )
    else:
        form = AppointLectureForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['lecture'] = lecture
            appoint_lecture.objects.create(**cleaned_data)

    ctx = {
        'lecture': lecture,
        'appoint': appoint_lecture,
        'form': form,
    }

    return render(request, 'appointment/lecture-detail.html', ctx)

def get_Station(request):
    ctx = {
        'station': Station.objects.all()
    }
    return render(request, 'appointment/station-list.html', ctx)

def get_Station_detail(request, station_id):
    name = request.session.get('username','')
    try:
        station = Station.objects.get(id=station_id)
    except Station.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = AppointStationForm(
            initial={'name': name}
        )
    else:
        form = AppointStationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['station'] = station
            appoint_lecture.objects.create(**cleaned_data)

    ctx = {
        'station': station,
        'appoint': appoint_station,
        'form': form,
    }
    return render(request, 'appointment/station-detail.html', ctx)