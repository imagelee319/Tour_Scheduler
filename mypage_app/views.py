from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from board.models import Board, Reply
from django.db import models


def index(request):
    if request.method == "POST":
        user = request.user
        user.username = request.POST["username"]
        user.save()
        return redirect("/")
    boards = Board.objects.all()
    reply = Reply.objects.all()
    context = {'boards':boards,"reply":reply}
    return render(request, 'mypage_app/mypage.html', context)


def UPDATEView(request):
    if request.method == 'GET':
        return render(request, 'mypage_app/update.html')

    elif request.method == 'POST':
        user = request.user

        email = request.POST.get('email')

        new_user_pw = request.POST.get('new_user_pw')


        user.email = email

        user.set_password(new_user_pw)

        user.save()


        return redirect('/', user.username)


# def home(request):
#
