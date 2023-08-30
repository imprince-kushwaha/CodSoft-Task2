from django.urls import path
from . import views

urlpatterns = [
    
    path('home/',views.home,name="home"),
    # path('signin/',views.signin,name="signin"),
    # path('login/',views.handleLogin,name="login"),
    path('about/',views.about),
    path('payment/',views.payment,name="pay"),
    path('user/',views.user,name="user"),
    path('contact/',views.contact1,name="contact"),
    # path('signup/',views.handleSignup,name="signup"),
    path('bookingsearchresult/',views.bkr,name="bkr"),
    path('thanks/',views.thanks,name="thanks"),
    path('bookingreceipt/',views.bookingreceipt,name="bookreceipt"),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('weather/',views.weather),
    path('mybooking/',views.mybooking,name="mybooking"),
]