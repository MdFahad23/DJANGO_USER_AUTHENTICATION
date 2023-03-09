from django.shortcuts import render
from Authentication import forms

# Create your views here.
def index(request):
    diction = {}
    return render(request, 'Authentication/index.html', context=diction)
    

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
