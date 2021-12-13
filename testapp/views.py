from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.
def homeview(request):
    return render(request,'testapp/home.html')
@login_required
def javaview(request):
    return render(request,'testapp/javaexams.html')
@login_required
def pythonview(request):
    return render(request,'testapp/pythonexams.html')
@login_required
def aptitudeview(request):
    return render(request,'testapp/aptitude.html')
def aboutus(request):
    return render(request,'testapp/aboutus.html')

def Exit(request):
    return render(request,'testapp/thanks.html')

def Signup(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
