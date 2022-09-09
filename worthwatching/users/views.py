from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from .forms import CustomUserCreationForm
from movies.models import Movie
# Create your views here.

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('movies')

    if request.method == 'POST':
        username = request.POST['username'].lower().strip()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User name doesn't exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('movies')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, "User logged out")
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid() == True:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            #Giving Permissions
            userid = User.objects.get(username=user.username)
            content_type = ContentType.objects.get_for_model(Movie)
            permission = Permission.objects.get(codename='modify_movie', content_type = content_type)

            #Add Permission
            # userid.user_permissions.add(permission)



            messages.success(request, 'User Account is created!')

            login(request, user)
            return redirect('/')

        else:
            messages.error(request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'login_register.html', context)

