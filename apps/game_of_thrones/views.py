from django.shortcuts import render, HttpResponse

def index(request):
    print 'in the method'
    return render(request,'game_of_thrones/index.html')
