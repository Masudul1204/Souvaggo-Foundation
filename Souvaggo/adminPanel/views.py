from django.shortcuts import render, redirect, HttpResponse
from adminPanel.models import home_insert, about_slider, about_slider_another, causes_slider
from adminPanel.models import sub_home_insert, volunteer_slider, news_slider
from adminPanel.models import User
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash

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

def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            old_pass = request.POST.get('old_pass')
            new_pass = request.POST.get('new_pass')
            confirm_pass = request.POST.get('confirm_pass')

            xyz = User.objects.get(id = request.user.id)
            if xyz.check_password(old_pass) and new_pass == confirm_pass:
                xyz.set_password(new_pass)
                xyz.save()
                update_session_auth_hash(request,xyz)
                return redirect('logout_user')
        return render(request, 'adminPanel/change-pass.html')
    else:
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
        show_home = home_insert.objects.all()
        return render(request,'adminPanel/home.html', {'show_home':show_home})
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
        show_about = sub_home_insert.objects.all()
        return render(request,'adminPanel/about.html', {'show_about': show_about})
    else:
        return render(request, 'adminPanel/login.html')


def about_Slider(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            x = request.POST.get('heading')
            y = request.POST.get('title')
            z = request.POST.get('Description')
            a = request.FILES['picture']
            
            about_slider_insert = about_slider(
                heading = x,
                title = y,
                Description = z,
                about_slider_pic = a
            )
            about_slider_insert.save()
        show_about_slider = about_slider.objects.all()
        return render(request,'adminPanel/about_slider_1.html', {'show_about_slider': show_about_slider})
    else:
        return render(request, 'adminPanel/login.html')

def about_Slider_another(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            y = request.POST.get('title')
            z = request.POST.get('Description')
            a = request.FILES['picture']
            
            about_slider_another_insert = about_slider_another(
                title = y,
                Description = z,
                about_slider_another_pic = a
            )
            about_slider_another_insert.save()
        show_about_slider_another = about_slider_another.objects.all()
        return render(request,'adminPanel/about_slider_2.html', {'show_about_slider_another': show_about_slider_another})
    else:
        return render(request, 'adminPanel/login.html')

def Causes(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            y = request.POST.get('causesTitle')
            z = request.POST.get('causesDescription')
            a = request.FILES['causesPicture']
            
            causes_slider_insert = causes_slider(
                title = y,
                Description = z,
                picture = a
            )
            causes_slider_insert.save()
        causes_slider_insert = causes_slider.objects.all()
        return render(request,'adminPanel/causes.html', {'causes_slider_insert': causes_slider_insert})
    else:
        return render(request, 'adminPanel/login.html')

def Volunteer(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            y = request.POST.get('volunteerTitle')
            z = request.POST.get('volunteerDescription')
            a = request.FILES['volunteerPicture']
            
            volunteer_slider_insert = volunteer_slider(
                title = y,
                Description = z,
                picture = a
            )
            volunteer_slider_insert.save()
        volunteer_slider_insert = volunteer_slider.objects.all()
        return render(request,'adminPanel/volunteer.html', {'volunteer_slider_insert': volunteer_slider_insert})
    else:
        return render(request, 'adminPanel/login.html')


def News(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            y = request.POST.get('newsTitle')
            z = request.POST.get('newsDescription')
            a = request.FILES['newsPicture']
            
            news_slider_insert = news_slider(
                title = y,
                Description = z,
                picture = a
            )
            news_slider_insert.save()
        news_slider_insert = news_slider.objects.all()
        return render(request,'adminPanel/news.html', {'news_slider_insert': news_slider_insert})
    else:
        return render(request, 'adminPanel/login.html')


def Contact(request):
    return render(request,'adminPanel/contact.html')

def about_slider_delete(request, id):
    about_slider_del = about_slider.objects.get(id=id)
    about_slider_del.is_delete = True
    about_slider_del.save()
    return redirect('about_slider')

