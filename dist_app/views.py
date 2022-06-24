from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'dist_app/dist_app.html')

def index_2(request):
    return render(request, 'dist_app/dist_app_2.html')

def index_3(request):
    return render(request, 'dist_app/dist_app_3.html')

def marker(request):
    return render(request, 'dist_app/dist_app_marker.html')

def jeju(request):
    return render(request, 'dist_app/1_jeju.html')

def aewol(request):
    return render(request, 'dist_app/2_aewol.html')

def hanlim(request):
    return render(request, 'dist_app/3_hanlim.html')

def hankyung(request):
    return render(request, 'dist_app/4_hankyung.html')

def daejung(request):
    return render(request, 'dist_app/5_daejung.html')

def andeok(request):
    return render(request, 'dist_app/6_andeok.html')

def jungmun(request):
    return render(request, 'dist_app/7_jungmun.html')

def seogwipo(request):
    return render(request, 'dist_app/8_seogwipo.html')

def namwon(request):
    return render(request, 'dist_app/9_namwon.html')

def pyosun(request):
    return render(request, 'dist_app/10_pyosun.html')

def seongsan(request):
    return render(request, 'dist_app/11_seongsan.html')

def gujwa(request):
    return render(request, 'dist_app/12_gujwa.html')

def jocheon(request):
    return render(request, 'dist_app/13_jocheon.html')