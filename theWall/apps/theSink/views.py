from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import *

def login(request):
    return render(request, 'theSink/login.html')

def registration(request):
    return render(request, 'theSink/registration.html')

def home(request):
    
    return render(request, 'theSink/home.html', {"recipes": Recipe.objects.all().order_by('-created_at') })

def viewRecipe(request):
    loggedIn = User.objects.loggedIn(request.POST)
    if loggedIn == False:
        request.session['userName'] = ''
        request.session['hashId'] = ''
        return redirect('/warning')
    else:
        print('user hash matches!!!')
        viewRecipe = Recipe.objects.get(name = request.POST['name'])
        request.session['recipeViewId'] = viewRecipe.id
        request.session['recipeViewName'] = viewRecipe.name
        request.session['recipeViewDesc'] = viewRecipe.desc
        request.session['recipeViewInst'] = viewRecipe.inst
        request.session['recipeViewIngr'] = viewRecipe.ingr
        return render(request, 'theSink/recipes.html', {"comments": Comment.objects.all().filter(recipe_id = request.session['recipeViewId']).order_by('-created_at')})

def validateLogin(request):
    errors = User.objects.loginValidator(request.POST)
    print('validating....', request.POST)
    if len(errors):
        print("in validate, found an error")
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')
    loggedUser = User.objects.get(userName = request.POST['userName'])
    if not bcrypt.checkpw(request.POST['password'].encode(), loggedUser.password.encode()):
        messages.error(request, 'Password or username is incorrect')
        return redirect('/login')
    else:
        print("in validate, found no error")
        request.session['userName'] = request.POST['userName']
        request.session['hashId'] = loggedUser.hashId
        return redirect('/home')

def validateReg(request):
    errors = User.objects.loginValidator(request.POST)
    print('validating....', request.POST['userName'])
    if len(errors):
        print("in validate, found an error")
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/registration')
    else:
        hashPW = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        hashID = bcrypt.hashpw(request.POST['userName'].encode(), bcrypt.gensalt())
        newUser = User(userName = request.POST['userName'], fName = request.POST['fName'], lName = request.POST['lName'], email = request.POST['email'], password = hashPW, hashId = hashID)
        newUser.save()
        loggedUser = User.objects.get(userName = request.POST['userName'])
        request.session['hashId'] = loggedUser.hashId
        request.session['userName'] = request.POST['userName']
        return redirect('/home')

def validateRecipe(request):
    loggedIn = User.objects.loggedIn(request.POST)
    if loggedIn == False:
        request.session['userName'] = ''
        request.session['hashId'] = ''
        return redirect('/warning')
    else:
        print('user hash matches!!!')
        errors = User.objects.recipeValidator(request.POST)
        print('validating....', request.POST)
        if len(errors):
            print("in validate, found an error")
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/home')
        else:
            print("in validate for recipes, found no error")
            # loggedUser = User.objects.get(userName = request.session['userName'])
            newRecipe = Recipe(name=request.POST['recipeName'], desc=request.POST['desc'], inst=request.POST['inst'], ingr=request.POST['ingr'], userId = User.objects.get(userName = request.session['userName']))
            newRecipe.save()
            return redirect('/home')

def logout(request):
    print('logged out', request.POST)
    request.session['userName'] = ''
    request.session['hashId'] = ''
    return redirect('/login')

def delete(request):
    print('YOU ARE FIRED!', request.session['userName'])
    x = request.session['hashId'].encode()
    deleteUser = User.objects.get(hashId = x)
    deleteUser.delete()
    return redirect('/logout')

def deleteRecipe(request):
    print('YOU ARE FIRED!', request.POST)
    loggedIn = User.objects.loggedIn(request.POST)
    if loggedIn == False:
        request.session['userName'] = ''
        request.session['hashId'] = ''
        return redirect('/warning')
    else:
        print('user hash matches!!!')
        deleteRec = Recipe.objects.get(name = request.POST['name'])
        deleteRec.delete()
        return redirect('/home')

def deleteComment(request):
    print('YOU ARE FIRED!', request.POST)
    deleteRec = Comment.objects.get(id = request.POST['id'])
    deleteRec.delete()
    return redirect('/home')

def editRecipe(request):
    loggedIn = User.objects.loggedIn(request.POST)
    if loggedIn == False:
        request.session['userName'] = ''
        request.session['hashId'] = ''
        return redirect('/warning')
    else:
        print('user hash matches!!!')
        print('editting', request.POST)
        return render(request, 'theSink/edit.html')

def edit(request):
    loggedIn = User.objects.loggedIn(request.POST)
    if loggedIn == False:
        request.session['userName'] = ''
        request.session['hashId'] = ''
        return redirect('/warning')
    else:
        print('user hash matches!!!')
        updatedRecipe = Recipe.objects.get(name = request.session['recipeViewName'])
        updatedRecipe.desc = request.POST['desc']
        updatedRecipe.ingr = request.POST['ingr']
        updatedRecipe.inst = request.POST['inst']
        updatedRecipe.save()
        return redirect('/home')

def validateComment(request):
    loggedIn = User.objects.loggedIn(request.POST)
    if loggedIn == False:
        request.session['userName'] = ''
        request.session['hashId'] = ''
        return redirect('/warning')
    else:
        print('user hash matches!!!')
        recipeId = Recipe.objects.get(name = request.POST['name'])
        userId = User.objects.get(userName = request.session['userName'])
        newComment = Comment(comment = request.POST['comment'], recipe_id = recipeId, user_id = userId)
        newComment.save()
        return redirect('/home')