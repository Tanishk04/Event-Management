from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='login') #login_required(redirect_field_name='next', login_url=None)
def HomePage(request):
    # return render(request, 'auth/home.html')
    if request.user.is_authenticated:
        return render(request, 'auth/profile.html',{'name' : request.user})
    else:
        return HttpResponseRedirect('/login/')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            return redirect('login')  #Redirigir a la vista de login

    return render(request, 'auth/signup.html')

def LoginPage(request):  #login(request, user, backend=None)
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1    = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('profile')  
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'auth/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')  
