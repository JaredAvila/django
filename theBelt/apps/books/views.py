from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
import bcrypt
import re
from itertools import chain

def books(request):
    books = Book.objects.all()
    reviews = BookReview.objects.all().order_by('-created_at')[:3]
    return render(request, 'books/books.html', {"books" : books, "reviews": reviews})

def validateBookReview(request):
    try:
        user1 = User.objects.get(hId=request.session['hId'])
    except:
        request.session['fName'] = ''
        request.session['hId'] = 'LoggedOut'
        errors = {
            "loggedOut": 'Error: Please login to access that feature'
        }
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
        return redirect('/login')
    if Book.objects.filter(title = request.POST['title']):
        errors= {
            "book": '***Book already exists, select title and then review***'
        }
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/books')
    book1 = Book(title=request.POST['title'], author=request.POST['author'])
    book1.save()
    review1 = BookReview(review=request.POST['review'], rating=request.POST['rating'], user_id=user1, book_id=book1)
    review1.save()
    print("validating review: ")
    return redirect('/books')

def validateReview(request):
    print(request.POST)
    user = User.objects.get(id = request.session['id'])
    book = Book.objects.get(id = request.session['bookId'])
    new = BookReview(review=request.POST['review'], rating=request.POST['rating'], user_id=user, book_id=book)
    new.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def show(request, id):
    request.session['fNameProf'] = User.objects.get(id = id).fName
    request.session['lNameProf'] = User.objects.get(id = id).lName
    request.session['emailProf'] = User.objects.get(id = id).email
    request.session['count'] = BookReview.objects.filter(user_id=id).count()
    return render(request, 'books/user.html', {"reviews": BookReview.objects.filter(user_id=id)})

def book(request, id):
    request.session['bookTitle'] = Book.objects.get(id=id).title
    request.session['bookAuthor'] = Book.objects.get(id=id).author
    request.session['bookId'] = id
    return render(request, 'books/book.html', {"reviews": BookReview.objects.filter(book_id = id)})

def delete(request, id):
    book = Book.objects.get(id=id)
    user = User.objects.get(id = request.session['id'])
    delBook = BookReview.objects.filter(book_id = book).filter(user_id = user)
    # delRev = BookReview.objects.get()
    
    delBook.delete()
    print('deleted. if not, query is whats up!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def logout(request):
    request.session['fName'] = ''
    request.session['hId'] = 'LoggedOut'
    print('User has been logged out. Thank you')
    return redirect('/login')