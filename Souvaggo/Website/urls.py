from django.urls import path
from Website import views

urlpatterns = [
    path('',views.index, name="main"),
    path('send_email',views.volunteer_email, name="send_email")
    
]