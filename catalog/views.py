
from django.shortcuts import render
def index(request):
    context ='index.html'
    return render(request, context)   