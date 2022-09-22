from django.shortcuts import render,redirect
from users.models import User
from django.contrib.auth import login, authenticate

# Create your views here.
def register(request):
    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profile_image = request.FILES.get('profile_image')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create(first_name = first_name,last_name=last_name, username=username       ,email=email,phone=phone,profile_image = profile_image)
            user.set_password(password)
            user.save()
            user = User.objects.get(username=username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
    return render(request, 'register.html')

def user_login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        user = authenticate(username = username,password = password)
        login(request, user)
        return redirect('index')
    return render(request, 'login.html')