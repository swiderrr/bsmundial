from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timezone
from mundial.models import Account
from mundial.forms import AccountAuthenticationForm

adj_list = open("mundial/utilities/adj_list.txt").read().splitlines()

def login_page(request):
    
    error_message = "Błędne dane logowania"

    user = request.user
    if user.is_authenticated:
        return redirect("homepage")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("homepage")
            else:
                return render(request, 'login_page.html', {'error_message': error_message})
    return render(request, 'login_page.html')

def start_page(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    else:
        return redirect('login_page')

def register_page(request):
    if request.method == 'POST':
        new_username = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        print("Pass1: " + pass1 + "\n")
        print("Pass2: " + pass2 + "\n")
        if not pass1 == pass2:
            return render(request,'register_page.html', {'wrong_pass': "Hasła się nie zgadzają!"})
        else:
            user = Account.objects.create_user(username=new_username, password=pass1)
            user.is_active = True
            user.save()
            print("username: " + user.username + "\n")
            print("password: " + user.password + "\n")
            return redirect('login_page')
    return render(request, 'register_page.html')

@login_required
def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    else:
        return redirect('login_page')

@login_required
def standings_page(request):
    if request.user.is_authenticated:
        user_list = Account.objects.all().order_by("points")
        return render(request, 'standings_page.html', {'user_list': user_list,
                                                  'adj_list': adj_list
                                                  })
    else:
        return redirect('login_page')