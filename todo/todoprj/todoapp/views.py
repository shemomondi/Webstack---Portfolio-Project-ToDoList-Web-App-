from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required
from .models import Profile
from todoapp.forms import ProfileEditForm
from django.shortcuts import get_object_or_404
from .models import todo
# from datetime import datetime

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
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
       
       
        # username = request.POST.get('username')
        
        # email = request.POST.get('email')
        
        # password = request.POST.get('password')
       
        # checking if the user's password is less than 3  characters long
        if len(password)<8:
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
        new_profile = Profile(user=new_user)
        new_profile.save()

        
        messages.success(request,"Registration Successful ! You can now login.")
        return redirect('login')
        
        
        # print(username)
    return render(request,'todoapp/register.html',{})

@login_required
def profile_view(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        # If the profile doesn't exist, create a new one
        profile = Profile(user=user)
        profile.save()

    if request.method == 'POST':
        # Update profile if form is submitted
        profile.bio = request.POST.get('bio', '')
        # Add other profile fields update here
        
        profile.save()

    return render(request, 'todoapp/profile.html', {'profile': profile})




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

@login_required
def create(request):
    if request.method == 'POST':
        # Get the user's input
        task = request.POST.get('task')
        # date_string = request.POST.get('date')  # Assuming the date input field name is 'date'
        description = request.POST.get('memo')

        # Parse the date string into a datetime object
        # try:
        #     date = datetime.strptime(date_string, "%Y-%m-%d")  # Adjust the format accordingly
        # except ValueError:
        #     # Handle invalid date format error
        #     # You might want to display a message to the user indicating the correct date format
        #     messages.error(request, 'Please enter a valid date in YYYY-MM-DD format')
        #     return redirect('create')  # Redirect the user back to the create page

        # Create a new todo item with the formatted date
        new_todo = todo(user=request.user, task=task, description=description)
        new_todo.save()

    # Fetch all todos for the current user
    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }
    
    return render(request, 'todoapp/create.html', context)

@login_required
def current(request):
    # Ensure the user is logged in
    if request.user.is_authenticated:
        # Retrieve todo items associated with the currently logged-in user
        all_todos = todo.objects.filter(user=request.user)
        context = {
            'todos': all_todos
        }
        return render(request, 'todoapp/current.html', context)
    else:
        # Redirect to the login page if the user is not logged in
        return redirect('login')
@login_required
def completed(request):
    # if(request.method == 'POST'):
    #     # Get the user's input and create a new todo item with it
    #     task = request.POST.get('completed')
    #     new_todo =  todo(user=request.user, todo_name=task) 
    #     new_todo.save()
    return render(request, 'todoapp/completed.html',{})
def my_view(request):
    return render(request, 'todoapp/todo.html', {'user': request.user})

@login_required
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'todoapp/profile_edit.html', {'form': form})

def delete_item(request, item_id):
    # Retrieve the item from the database
    item = get_object_or_404(todo, pk=item_id)
    # Delete the item
    item.delete()
    # Redirect to a suitable page (e.g., homepage or list of items)
    return redirect('current')

def update_status(request, item_id):
    # Retrieve the item from the database
    item = get_object_or_404(todo, pk=item_id)
    # Toggle the status (if it's True, set to False; if False, set to True)
    item.status = not item.status
    # Save the changes
    item.save()
    # Redirect to a suitable page (e.g., homepage or list of items)
    return redirect('current')
def completed(request):
    todos = todo.objects.filter(status=False)  # Get active/in-progress tasks
    completed_tasks = todo.objects.filter(completed=True)  # Get completed tasks
    return render(request, 'todoapp/completed.html', {'todos': todos, 'completed': completed_tasks })

