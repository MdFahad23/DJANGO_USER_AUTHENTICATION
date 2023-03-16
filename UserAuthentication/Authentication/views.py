from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse


from Authentication import forms
from django.contrib.auth.models import User

# Create your views here.

# Home View
def index(request):
    diction = {}

    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id

        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = forms.UserInfo.objects.get(user__pk=user_id)

        diction = {'user_basic_info': user_basic_info, 'user_more_info': user_more_info}
        
    return render(request, 'Authentication/index.html', context=diction)

# Login View
def Login_page(request):
    return render(request, 'Authentication/login.html')

# User Login
def User_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("Authentication:index"))
            else:
                return HttpResponse("Account is not Active!")
        else:
            return HttpResponse('Login Details are Wrong!')
        
    else:
        return render(request, 'Authentication/index.html')
    

# User Logout
@login_required
def User_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("Authentication:index"))

# User Register View
def register(request):

    registered = False

    if request.method == 'POST':
        user_from = forms.UserFrom(data=request.POST)
        user_info_from = forms.UserInfoFrom(data=request.POST)

        if user_from.is_valid() and user_info_from.is_valid():
            user = user_from.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_from.save(commit=False)
            user_info.user = user

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']

            user_info.save()
            registered = True

    else:
        user_from = forms.UserFrom()
        user_info_from = forms.UserInfoFrom()


    diction = {'user_from': user_from, 'user_info_from': user_info_from, 'registered': registered}
    return render(request, 'Authentication/authentication.html', context=diction)
