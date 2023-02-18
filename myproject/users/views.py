from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache

# Create your views here.


@never_cache
def homepage(request):
    if 'username' in request.session:
        return render(request, 'homepage.html')
    else:
        return redirect('login')


@never_cache
def user_login(request):
    if 'username' in request.session:
        return redirect('homepage')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            return redirect('homepage')
        else:
            print('invalid ')
    return render(request, 'loginpage.html')


def user_logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('login')


def register(request):
    if 'username' in request.session:
        return redirect('homepage')
    #Register Page
    if request.method=='POST':
        reg_username=request.POST['username']
        reg_email=request.POST['email']
        reg_password1=request.POST['password1']
        reg_password2=request.POST['password2']
        print(reg_username)
        if reg_password1 == reg_password2:
            if User.objects.filter(username=reg_username).exists():
                return render(request, 'register.html')

            elif User.objects.filter(email=reg_email).exists():
                return render(request, 'register.html')

            else:
                user=User.objects.create_user(username=reg_username,password=reg_password1,email=reg_email)
                user.save()
                return redirect('homepage')

        else:
            print('Password not matching')
            return render(request, 'register.html')

    else:
        return render(request,'register.html')
