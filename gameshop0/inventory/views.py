from django.shortcuts import render
from inventory.models import Customer,Game,Assign
from inventory.forms import NewCustomerForm,AssigningForm,AddGameForm,UserForm


#special login imports
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request , "index.html")

def user_login(request):

    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("passwd")

        user = authenticate(username = username , password = password)

        if user:
            if user.is_active:
                login(request , user)
                return customerinfo(request)

            else:
                return HttpResponse("ACCOUNT NOT Active")

        else:
            return HttpResponse("Invaild username and password")

    else:
        return render(request, 'login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return index(request)


def register(request):
     registered = False
     user_form = UserForm()
     if request.method == "POST":
         user_form = UserForm(request.POST)

         if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
         else:
             print(user_form.error)


     return render(request, "register.html" , {'user_form':user_form , 'registered':registered})

def addgame(request):
    form = AddGameForm()
    if request.method == "POST":
        form = AddGameForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return game(request)
        else:
            print("Error input Invalid ")

    return render(request , "addGame.html" , {'form':form})

def gamereturn(request , customer_email , game_type):
    Assign.objects.filter(customer_phone__email = customer_email ).filter( game_name__game_type = game_type).delete()
    return game(request)

def game(request):

    game_list = Game.objects.order_by('game_name')
    status = Assign.objects.order_by('game_name')
    game_dict = {'game_info' : game_list , 'status' : status  }

    return render(request , "game.html" , context = game_dict)


def assign(request):
    form = AssigningForm()
    if request.method == "POST":
        form = AssigningForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return game(request)
        else:
            print("Error input Invaild")
    return render(request , "assign.html" , {'form':form})

def signup(request):
    form = NewCustomerForm()

    if request.method == "POST":
        form = NewCustomerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return customerinfo(request)
        else:
            print("Error from Invaild")

    return render(request , "signup.html" , {'form':form})

def customerinfo(request):
    customer_list = Customer.objects.order_by('name')
    customer_dict = {'customer_info' : customer_list}
    return render(request , "customerinfo.html" , context = customer_dict)
