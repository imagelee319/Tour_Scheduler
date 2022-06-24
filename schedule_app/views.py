
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from . import models
from .models import Adddate, Hotplace
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def index(request):
    return render(request, 'schedule_app/schedule_list.html')


def schedulelist(request):
    during = Adddate.objects.filter(author_id=request.user)

    return render(request, 'schedule_app/schedule_list.html', {'during': during})


# def finallist(request):
#     place_list = Hotplace.objects.filter(tour=Adddate.objects.filter(author_id=request.user))
#     return render(request, 'schedule_app/schedule_list.html', {'place_list': place_list})

def finallist(request):
    hotplace_list = Hotplace.objects.filter(place_author_id=request.user).order_by('days')
    return render(request, 'schedule_app/schedule_list.html', {'hotplace_list': hotplace_list})


def create(request):
    during = Adddate(during=request.GET.get('during'), author=request.user)
    during.save()

    during1 = request.GET.get('during')
    days = list(range(int(during1)))
    days1 = []
    for i in days:
        days1.append(i + 1)

    return render(request, 'schedule_app/schedule_list.html', {'day': days1, 'tour_id': during.pk})
    # return redirect('/schedule_app/list')


def day(request):
    if request.GET.get('place') != None:
        place = Hotplace(tour_place=request.GET.get('place'), days=request.GET.get('test'), tour_id=request.GET.get('fk'), place_author=request.user)
        place.save()

        return redirect('/schedule_app/finallist')


def delete(request, place_author_ad):
    place_list = Hotplace.objects.get(id=place_author_ad)
    place_list.delete()
    return redirect('/schedule_app/finallist')



