from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        firstName=request.POST['fname']
        lastName=request.POST['lname']
        userName=request.POST['uname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1==pass2:
            if User.objects.filter(username=userName).exists():
                messages.info(request,'UserName already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email ID already exists')
                return redirect('register')
            else:

                u=User.objects.create_user(username=userName,first_name=firstName,last_name=lastName,email=email,password=pass1)
                u.save()
                messages.info(request,"You have successfully registerd!")
                return render(request,'index.html')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
    else:
        return render(request,'register.html')




def login(request):
        if request.method=='POST':
            uname=request.POST['username']
            password=request.POST['password']
            u=auth.authenticate(username=uname,password=password)
            if u is not None:
                request.session['uid']=u.id
                auth.login(request,u)
                return redirect("/")
            else:
                messages.info(request,"Login fail! Invalid credentials")
                return redirect("login")
        else:
            return render(request,'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,"You have logged out! Visit Again")
    return redirect("/")