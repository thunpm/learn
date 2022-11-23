from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import User


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        passsword = request.POST['password']
        user = User.objects.filter(email=email, passsword=make_password(passsword)).first()
        if user:
            return render(request, 'home.html')
        else:
            return render(request, 'login.html', {"msg": "Tai khoan khong chinh xac"})
    else:
        return render(request, 'login.html')
