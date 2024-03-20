from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import todo

# Create your views here.
def home(request):
    # if(request.method == 'POST'):
    #     # Get the user's input and create a new todo item with it
    #     task = request.POST.get('task')
    #     new_todo =  todo(user=request.user, todo_name=task) 
    #     new_todo.save()
    return render(request, 'todoapp/todo.html',{})

# Getting user's data from the registration page and validating it with Django authentication system.
def register(request):
    #checking if the  request method is a POST from user's submitted form
    if request.method == 'POST':
       #if the above is true  then get the username and password entered by the user in the form using name attribute specified in the form
        username = request.POST.get('username')
        
        email = request.POST.get('email')
        
        password = request.POST.get('password')
       
        # checking if the user's password is less than 3  characters long
        if len(password)<3:
            messages.error(request,'Password is too short!')
            return redirect('register') 
        
        #checking if the user already exist by first getting all the users and then  filter to find a matching
        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request,"Username already exists")
            return redirect('login')
       
       #Then if the user do not  exist in database we create new user using Django authentication system.
        new_user = User.objects.create_user(username=username, password=password, email=email)
        new_user.save()
        # After creating the user we log him in to the log in page in order to retype his/her details  into login form to get access to the home page 
        
        messages.success(request,"Registration Successful ! You can now login.")
        return redirect('login')
        
        
        # print(username)
    return render(request,'todoapp/register.html',{})
def loginpage(request):
    #checking if the  request method is a POST from user's submitted form
    if request.method == 'POST':
       #if the above is true  then get the username and password entered by the user in the form using name attribute specified in the form
        username = request.POST.get('uname')

        password = request.POST.get('pass')
        
        #checking if the user already exist in the database
        validate_user = authenticate(username=username, password=password)
        #so if user  does not exist or wrong password show error message else log in the user.
        if validate_user is not None:
            login(request,validate_user)#remember we have used the login  function which comes with Django Authentication System which we have imported up in this code
            
            #Now that we have confirmed that the user do not exist  and the password is correct
            #let us now allow him/her to access the home page
            
            return redirect('home_page')#rem this 'home page' used here is from  urls.py file where i defined it as home_page as the name atribute 
        else: #So if ther is not on the database  then raise an error message that  the user name or password was incorrect.
            messages.error(request,'Wrong username or Password please  try again ')
            return redirect('login')#Now let us give them a chance to retype there details again
            
        
        
       #Then if the user do not  exist in database we create new user using Django authentication system.
        # new_user = User.objects.create_user(username=username, password=password, email=email)
        # new_user.save()
        
        # print(username)
    return render(request,'todoapp/login.html',{})


def create(request):
    if(request.method == 'POST'):
        # Get the user's input and create a new todo item with it
        task = request.POST.get('task')
        date = request.POST.get('date')
        description = request.POST.get('memo')
        new_todo =  todo(user=request.user, task=task, date=date , description=description) 
        new_todo.save()
        
    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }
   
         
    return render(request, 'todoapp/create.html',context)

def current(request):
    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }
    return render(request, 'todoapp/current.html', context)

def completed(request):
    # if(request.method == 'POST'):
    #     # Get the user's input and create a new todo item with it
    #     task = request.POST.get('completed')
    #     new_todo =  todo(user=request.user, todo_name=task) 
    #     new_todo.save()
    return render(request, 'todoapp/completed.html',{})