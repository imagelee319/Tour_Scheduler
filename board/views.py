from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Board


@login_required(login_url='accounts:login')
def index(request):
    all_boards = Board.objects.all().order_by("-pub_date")  # 모든 데이터 조회, 내림차순(-표시) 조회
    paginator = Paginator(all_boards, 5)
    page = int(request.GET.get('page', 1))
    board_list = paginator.get_page(page)
    return render(request, 'board/index.html', {'title': 'Board List', 'board_list': board_list})


@login_required(login_url='accounts:login')
def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    return render(request, 'board/detail.html', {'board': board})

@login_required(login_url='accounts:login')
def write(request):
    return render(request, 'board/write.html')

@login_required(login_url='accounts:login')
def write_board(request):
    b = Board(title=request.POST['title'], content=request.POST['detail'], author=request.user, pub_date=timezone.now())
    b.save()
    return HttpResponseRedirect(reverse('board:index'))

@login_required(login_url='accounts:login')
def create_reply(request, board_id):
    b = Board.objects.get(id = board_id)
    b.reply_set.create(comment=request.POST['comment'], rep_date=timezone.now(), author = request.user)
    return HttpResponseRedirect(reverse('board:detail', args=(board_id,)))


@login_required(login_url='accounts:login')
def delete(request, pk):
    post = Board.objects.get(id=pk)
    post.delete()
    return redirect('board')

@login_required(login_url='accounts:login')
def edit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.writer = request.POST['writer']

        board.save()
        return redirect('board')

    else:
        boardForm = Board
        return render(request, 'update.html', {'boardForm':boardForm})
