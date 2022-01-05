from django.forms.widgets import PasswordInput
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Signup
from . forms import SignupForm,LoginForm,UpdateForm
from django.contrib import messages
from django.contrib.auth import logout as logouts



# Create your views here.
def index(request):
    var1 = "vishwa"
    return render(request,'index.html',{'data':var1})
def register(request):
    if request.method=='POST':
        form=SignupForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            name = form.cleaned_data['Name']
            age = form.cleaned_data['Age']
            place = form.cleaned_data['Place']
            photo = form.cleaned_data['Photo']
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            cpassword = form.cleaned_data['Confirmpassword']
            user = Signup.objects.filter(Email=email).exists()
            
            if user:
               messages.warning(request,"user already exist")
               return redirect('request')
            elif cpassword!=password:
                messages.warning(request,"password mismatch")   
                return redirect('register/')
            else:
                tab = Signup(Name=name,Age=age,Place=place,Email=email,Password=password,Photo=photo)
                tab.save()
                messages.success(request,"registration successfull")
                return redirect('/')
        
    else:
        form = SignupForm()
    return render(request,'register.html',{'form':form})
def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            user=Signup.objects.get(Email=email)
            if not user:
                messages.warning(request,"email does not exist")
                return redirect('login/')
            elif user.Password !=password:
                messages.warning(request,'incorrect password')
                return redirect('login/')
            else:
                messages.success(request, "login successfull")
                return redirect('/home/%s'% user.id)
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})
        
def home(request,id):
    user = Signup.objects.get(id=id)
    return render(request,'home.html',{'user':user})

def update(request,id):
    user = Signup.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,request.FILES or None,instance=user)
        if form.is_valid():
            form.save()
    
            messages.success(request,"updated successfully")
            return redirect("/home/%s" % user.id)
    else:
        form=UpdateForm(instance=user)
            
    
    return render(request,'update.html',{'user':user,'form':form})
def logout(request):
    logouts(request)
    messages.success(request,"loggedout successfully")
    return redirect('/')
