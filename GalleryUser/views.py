from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from GalleryUser.models import User, UserManager
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.contrib import messages


# Create your views here.
@csrf_exempt
def gallery_login(request):
    if request.method == 'GET':
        return render(request, "login.html")

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if len(username) == 0 or len(password) == 0:
            messages.add_message(request, messages.INFO, 'write correctly')
            return render(request, "login.html")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print(user, "Login", timezone.now)
            return redirect("/auth/profile")

        return redirect("/")


@csrf_exempt
def join(request):
    if request.method == 'GET':

        return render(request, "join.html")

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        e_mail = request.POST['e_mail']

        user = User.objects.filter(username=username).values()

        if len(user) > 0:
            return redirect('/auth/join')

        if password != confirmPassword:
            return redirect('/auth/join')

        user = User.objects.create_user(username=username, password=password, e_mail=e_mail)

        return redirect('/auth/login')


@login_required
def user_profile(request):
    user = request.user

    context = {'user': user}

    return render(request, "profile.html", context)
