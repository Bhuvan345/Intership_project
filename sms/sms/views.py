from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, logout, login
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth.decorators import login_required
from app.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')


@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name

            if password != None and password != '':
                customuser.password = password
            customuser.save()
            messages.success(
                request, 'Your profile is updated successfully !!')
            redirect('profile')
        except:
            messages.error(request, 'Error in updating the profile !!')
    return render(request, 'profile.html')


def doLogout(request):
    logout(request)
    return redirect('login')


def doLogin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),)
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('Hod_home')
            elif user_type == '2':
                return HttpResponse('this is staff ')
            elif user_type == '3':
                return HttpResponse('this is student ')
            else:
                # Message
                return redirect('login')
        else:
            # Message
            return redirect('login')
