from django.urls import path
from Website import views

urlpatterns = [
    path('',views.index, name="home"),
    
]