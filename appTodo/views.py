from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import todoitem
# Create your views here.
def index(request):
    items = todoitem.objects.all()
    return render(request, 'index.html', context={'items': items})

def additem(request):
    print(request.POST['text'])
    text = request.POST['text']
    text = todoitem(text=text)
    text.save()
    return HttpResponseRedirect('/')

