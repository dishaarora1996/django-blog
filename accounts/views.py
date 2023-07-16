from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not User.objects.filter(email=email).exists():
            messages.error(request, 'Account does not exist')
        else:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Email or Password is incorrect')

    return render(request, 'login.html')



def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        image_file = request.FILES.get('image')
        if image_file is None:
            image_file = 'profiles/user-default.png'
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        else:
            user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, profile_image=image_file)
            messages.success(request,"Registion successful. Kindly login.")

        print(first_name, last_name, email, password, image_file)
        return redirect('register_user')
    return render(request, 'register.html')



def logout_user(request):
    logout(request)
    return redirect('login_user')