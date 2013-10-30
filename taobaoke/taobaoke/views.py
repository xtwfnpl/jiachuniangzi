from django.http import HttpResponse
from django.shortcuts import render_to_response

def mainpage(request):
    #return HttpResponse("hello")
    return render_to_response('mall.html')