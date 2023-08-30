from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from travelbook.models import Contact
from travelbook.models import Flights
from travelbook.models import Booking
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
   return render(request,"index.html")

def weather(request):
   return render(request,"weather.html")
   
   
def about(request):
   return render(request,"about.html")

@login_required(login_url='')
def payment(request):
   return render(request,"payment.html")

def thanks(request):
   return render(request,'thanks.html')

def mybooking(request):
   return render(request,'mybooking.html')

def bookingreceipt(request):
   return render(request,'bookingreceipt.html')

# @login_required(login_url='')
# def HomePage(request):
#     return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        #for checking if both password are same or not if not then no login
        if pass1!=pass2:
            return HttpResponse("your password and confirm is not same")
        else:   
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            #return HttpResponse("user has created successfully!!!!!!!!!!") to check if signup working or not
            return redirect('login')#ye login ke andar ke url ka page h and redirect to login



        #print(uname,email,pass1,pass2) to check if it is taking and printing or not
    return render (request,'signup.html')#display hoga jb hm '' se server run krenge

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:   #means agr upr wale me kuch bhi aaya to ye chal jaega
            login(request,user)
            return redirect('user')  #redirect kr denge home ke andar agr login ho gye to
        else:
            return HttpResponse("user or password is wrong")  #agr glt hoga to ye mssg print hoga

        #print(username,pass1) to confirm ki data aa bhi rha h ki nhi

    return render (request,'login.html')#jb login/ se runserver krenge

def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='')
def user(request):
   
   return render(request,"user.html")

def contact1(request):


   if request.method=='POST':
      #always keep different names of key in different forms eg,contact-username in contact form and username in signup
      username=request.POST.get('contact-username')
      email=request.POST.get('contact-email')
      phone=request.POST.get('contact-phone')
      message=request.POST.get('contact-message')
      contact=Contact(username=username,email=email,phone=phone,message=message)
      contact.save()
      return redirect('home')
   else:
      return HttpResponse("something went wrong")
   return render(request,"index.html")
@login_required(login_url='')
def bkr(request):
   
   flightdata=Flights.objects.all()
   
   
   
   bookdata=Booking.objects.all()
      
   data={
      'flightdata':flightdata,
      'bookdata':bookdata,
      
   }
   
   return render(request,'booking.html',data)


def bookingreceipt(request):
   a=[1000,1200,1350,1500]
   flightdata=Flights.objects.all()
   for i in flightdata:
      
      print(i.price)
      
   
   bookdata=Booking.objects.all()
      
   data={
      'flightdata':flightdata,
      'bookdata':bookdata,
      'a':a
      
      
   }
   return render(request,'bookingreceipt.html',data)
