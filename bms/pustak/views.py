from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Book 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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

def delete_book(request, id):
    data = Book.objects.get(id=id)
    data.delete()
    return redirect('/')

def update_book(request, id):
    queryset = Book.objects.get(id=id)
    if request.method == "POST":
        bn = request.POST.get('book_name')
        bd = request.POST.get('book_description')
        bi = request.FILES.get('book_image')

        queryset.book_name = bn
        queryset.book_description = bd  
        if bi:
            queryset.book_image = bi
        queryset.save()
        return redirect('/')
    context = {'book':queryset}
    return render(request, 'pustak/updatebooks.html',context)






def register_page(request):
    if request.method == "POST":
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        un = request.POST.get('username')
        pw = request.POST.get('password')
        if not fn or not ln or not un or not pw:
            messages.error(request, 'All fields are required.')
            return render(request, 'pustak/register.html')
        
        if User.objects.filter(username=un).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'pustak/register.html')

        User.objects.create_user(first_name=fn,last_name=ln,username=un,password=pw)
        messages.success(request, 'Registration successful!')
        return redirect('/login/')

    return render(request, 'pustak/register.html')
    

def login_page(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pw = request.POST.get('password')
        # Add login logic here
        user = authenticate(username=un, password=pw)
        if user is not None:
           messages.error(request, 'Login Failed! Please check your username and password')
           return redirect('/login/')        
        else:
            login(request, user)
    return render(request, 'pustak/login.html')

def logout_page(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login/')