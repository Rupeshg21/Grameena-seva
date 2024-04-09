from django.shortcuts import render
from seva.models import Newreg
from seva.forms import Newregform
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'seva/home.html')

@login_required
def pan(request):
    return render(request,'seva/pan.html')


def newr(request):
    form=Newregform()
    if request.method == 'POST':
        form=Newregform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'seva/home.html')
    return render(request,'seva/newr.html',{'form':form})



def logout(request):
    return render(request,'seva/logout.html')

def list(request):
    list=Newreg.objects.all()
    return render(request,'seva/list.html',{'list':list})
