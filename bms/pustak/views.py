from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def books(request):
    # return HttpResponse("Welcome to django")
    return render(request, 'books.html')