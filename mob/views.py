from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,logout,authenticate
from.models import*

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method=="POST":
        email_n=request.POST.get("email")
        password_n=request.POST.get("password")
        user1=authenticate(username=email_n,password=password_n)
        print(user1)
        if not user1:
            print("User not found")
        else:
            print("User found")
            auth_login(request,user1)
            print(request.user1)
        return render(request,'receipt.html')
    return render(request, "login.html")

def signup(request):
    if request.method=="POST":
        first_n=request.POST.get('fName',None)
        last_n=request.POST.get('lName',None)
        email_n=request.POST.get('email',None)
        password_n=request.POST.get('password',None)
        user=User.objects.create_user(username=email_n,email=email_n,first_name=first_n,last_name=last_n,password=password_n)
        return render(request, "login.html")
    return render(request, "signup.html")

def receipt(request):
    if request.method == "POST":
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        course=request.POST.get("course")
        duration=request.POST.get("duration")
        # phone=request.POST.get("Phone")
        address=request.POST.get("address")
        city=request.POST.get("city")
        zipcode=request.POST.get("zipp")

        Receipt.objects.create(Fname=fname,Lname=lname,Email=email,Password=password,Course=course,Duration=duration,Address=address,City=city,Zipcode=zipcode,user=request.user)


    return render(request, "receipt.html")

def viewreceipt(request):
    receipt=Receipt.objects.all()
    context={'receipt':receipt}
    print(receipt)
    return render(request,'viewrec.html',context)

def deletereceipt(request,pk):
    Receipt.objects.filter(id=pk).delete()
    receipt=Receipt.objects.all()
    context={'receipt':receipt}
    return render(request,'viewrec.html',context)
