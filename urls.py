from django.urls import path
from .import views

urlpatterns=[
    path('home/', views.home,name="home"),
    path('gallery/', views.gallery,name="gallery"),
    path('register/', views.register,name="register"),
    path('admindashboard/', views.admindashboard,name="admindashboard"),
    path('login/', views.login,name="login"),
    path('signup/', views.signup, name="signup"),

]