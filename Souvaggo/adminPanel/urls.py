from django.urls import path
from adminPanel import views

urlpatterns = [
    path('admin',views.index, name="admin"),
    path('login',views.login_page, name="login_page"),
    path('reg',views.reg_page, name="reg_page"),
    path('logout_user',views.logout_page, name="logout_user"),
    path('home',views.home, name="home"),
    path('about',views.About, name="about"),
    path('about_slider',views.about_Slider, name="about_slider"),
    path('about_slider_another',views.about_Slider_another, name="about_slider_another"),
    path('causes',views.Causes, name="causes"),
    path('volunteer',views.Volunteer, name="volunteer"),
    path('news',views.News, name="news"),
    path('contact',views.Contact, name="contact"),
    # path('test',views.insert_show_home, name="test"),

]