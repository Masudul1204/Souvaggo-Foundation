from django.shortcuts import render, redirect
from adminPanel.models import home_insert
from adminPanel.models import sub_home_insert
from django.conf import settings
from django.core.mail import send_mail

def index(request):
    insert_home_show =home_insert.objects.all()
    insert_sub_home_show = sub_home_insert.objects.all()
    context = {
        'insert_home_show' : insert_home_show,
        'insert_sub_home_show' : insert_sub_home_show

    }
    return render(request,'website/index.html', context)

def volunteer_email(request):
    if request.method == 'POST':
        name = request.POST.get('volunteer_name')
        email = request.POST.get('volunteer_email')
        subject = request.POST.get('volunteer_subject')
        massage = request.POST.get('volunteer_message')

        final_massage = massage + ' ' + name + ' ' + email
        from_email = settings.EMAIL_HOST_USER
        to_email = ['eng.mohammadmasud@gmail.com','fmnasim18@gmail.com']

        send_mail(subject, final_massage, from_email, to_email)
        return redirect('main')




