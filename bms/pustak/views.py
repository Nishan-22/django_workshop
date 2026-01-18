from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Book

# Create your views here.
def books(request):
    # return HttpResponse("Welcome to django")
    if request.method == "POST": 
        bn = request.POST.get('book_name')
        bd = request.POST.get('book_description')
        bi = request.FILES.get('book_image')
        Book.objects.create(book_name = bn, book_description = bd, book_image = bi)
        return redirect('/')
    queryset = Book.objects.all()
    context = {'books': queryset}

    return render(request, 'pustak/books.html', context)