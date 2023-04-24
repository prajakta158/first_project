from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from .models import Book
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .form import BookForm

@login_required
def home(request):
    print(request.method)   #GET
    if request.method == 'POST' :
        data = request.POST
        bid = data.get("book_id") 
        name = data.get("Book_name")
        qty=  data.get("Book_qty")
        price = data.get("Book_price")
        author = data.get("Book_author")
        if not bid :
            Book.objects.create(name=name, qty=qty, price=price, author=author)
        else:
            book_obj = Book.objects.get(id=bid)
            book_obj.name = name
            book_obj.qty = qty
            book_obj.price = price
            book_obj.author = author
            book_obj.save()
        
        # print(Book)
    return render(request, "home.html")

@login_required
def show_books(request):
    # Book.objects.all()
    return render(request, "show_book.html",{"books": Book.objects.filter(is_active=True)})

def update_books(request, pk):
    book_obj = Book.objects.get(id=pk)
    return render(request, "home.html", context={"single_book": book_obj})

def delete_book(request, pk):   #1  - # 2 link in show_book
    Book.objects.get(id=pk)
    return render('all_inactive_books')

def soft_delete_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.is_active = False
    book_obj.save()  
    return redirect("all_inactive_books")

@login_required
def show_inactive_books(request):  # 1
    return render(request, "show_book.html", {"books": Book.objects.filter(is_active=False), "inactive":True})

def restore_book(request, pk):  # here we hv to reverser the process of soft del
    book_obj = Book.objects.get(id=pk)
    book_obj.is_active = True
    book_obj.save()
    return redirect("show_books")

def book_form(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect("Book_login")
    form = BookForm()
    return render (request=request , template_name="book_form.html" , context={"register_form":form})


def book_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request , user)
                return redirect("home_page")
            else:
                return redirect("book_login")
        else:
            return redirect("home_page")
    form = AuthenticationForm()
    return render(request=request , template_name="book_login.html",context={"login_form":form})

def logout_user(request):
    logout(request)
    return redirect("book_login")