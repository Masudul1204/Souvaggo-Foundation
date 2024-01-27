from django.shortcuts import render
from adminPanel.models import home_insert
from adminPanel.models import sub_home_insert

def index(request):
    insert_home_show =home_insert.objects.all()
    insert_sub_home_show = sub_home_insert.objects.all()
    context = {
        'insert_home_show' : insert_home_show,
        'insert_sub_home_show' : insert_sub_home_show

    }
    return render(request,'website/index.html', context)

# def home_index(request):
#     insert_sub_home_show = sub_home_insert.objects.all()
#     return render(request,'website/index.html', {'insert_sub_home_show': insert_sub_home_show})



