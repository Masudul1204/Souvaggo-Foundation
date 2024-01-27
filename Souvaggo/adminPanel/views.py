from django.shortcuts import render, redirect, HttpResponse
from adminPanel.models import home_insert
from adminPanel.models import sub_home_insert
from adminPanel.models import User
from django.contrib.auth import login,logout,authenticate

def index(request):
    if request.user.is_authenticated:
        return render(request, 'adminPanel/index.html')
    else:
        return redirect('login_page')
def reg_page(request):
    if request.method == 'POST':
        user_name = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('re_password')
        if password != repassword:
            return redirect('reg_page')
        else:
            user_reg = User.objects.create_user(user_name,email,password)
            user_reg.last_name = 'Islam'
            user_reg.save()
            return redirect('login_page')
    return render(request, 'adminPanel/reg.html')

def login_page(request):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('password')
        user = authenticate(username = a, password = b)
        print(user)
        if user != None:
            login(request,user)
            return redirect('admin')
        else:
            return redirect('login_page')
    if request.user.is_authenticated:
        return redirect('admin')
    else:
        return render(request, 'adminPanel/login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')




def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            x = request.POST.get('home_title')
            y = request.POST.get('home_slogan')
            z = request.FILES['home_pic']
            
            home_info = home_insert(
                home_title = x,
                home_slogan = y,
                home_pic = z
            )
            home_info.save()
        return render(request,'adminPanel/home.html')
    else:
        return render(request, 'adminPanel/login.html')

def About(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            y = request.POST.get('short_title')
            z = request.POST.get('sub_short_title')
            a = request.FILES['picture']
            
            sub_home_info = sub_home_insert(
                short_title = y,
                sub_short_title = z,
                home_pic = a
            )
            sub_home_info.save()
        return render(request,'adminPanel/about.html')
    else:
        return render(request, 'adminPanel/login.html')

def Causes(request):
    return render(request,'adminPanel/causes.html')

def Volunteer(request):
    return render(request,'adminPanel/volunteer.html')

def News(request):
    return render(request,'adminPanel/news.html')

def Contact(request):
    return render(request,'adminPanel/contact.html')

