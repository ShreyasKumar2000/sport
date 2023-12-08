from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Football
from . forms import FootballForm
# Create your views here.
def index(request):
    football=Football.objects.all()
    context={
        'footballer':football
    }
    return render(request,'index.html',context)

def detail(request,football_id):
    football=Football.objects.get(id=football_id)
    return render(request,"detail.html",{'football':football})

def add_football(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        club=request.POST.get('club')
        bdor=request.POST.get('bdor')
        img=request.FILES['img']
        football=Football(name=name,desc=desc,club=club,bdor=bdor,img=img)
        football.save
    return render(request,'add.html')

def update(request,id):
    football=Football.objects.get(id=id)
    form=FootballForm(request.POST or None,request.FILES,instance=football)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'football':football})

def delete(request,id):
    if request.method=="POST":
        football = Football.objects.get(id=id)
        football.delete()
        return redirect('/')
    return render(request,'delete.html')