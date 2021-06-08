from django.shortcuts import render, redirect
from .forms import UploadBookForm
from .models import EBooksModel
from django.http import HttpResponse
from django.contrib.auth.models import User


#=== after login ====
#1. upload_book
#2. book_list
#3. delete_book


# # # after login


def upload_book(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UploadBookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # books = EBooksModel.objects.all()
                # return render(request, 'book_list.html', {'books': books})
                return redirect('/')
        else:
            form = UploadBookForm()
            context = {
                'form': form,
            }
        return render(request, 'ebook/upload_book.html', context)
    else:
        return redirect('/user_login/')


def book_list(request):
    # if request.user.is_authenticated:
        # if request.user.is_superuser:
        books = EBooksModel.objects.all()
        return render(request, 'ebook/book_list.html', {'books': books, 'user':request.user})
    # else:
        # return redirect('/user_login/')



def delete_book(request, id):
    if request.method == "POST":
        book = EBooksModel.objects.get(pk = id)
        print(request.user)
        if request.user.username == book.author:    
            book.delete()
        elif request.user.is_superuser:
            book.delete()
        else:
            HttpResponse("you have not delete permission")
        return redirect('/')
        

        



def get_user_profile(request, username):
    user = User.objects.get(username=username)
    user_books = EBooksModel.objects.filter(author=username)#.all(uploaded_by=username)
    print("user_books", user_books)
    return render(request, 'registration/user_profile.html', {"user":user, "user_books": user_books})




        
def search(request):        
    search =  request.GET['search']    
    books = EBooksModel.objects.filter(titlee__icontains=search)
    return render(request,"ebook/search.html",{"books":books})
        













