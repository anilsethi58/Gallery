from django.shortcuts import render
from .forms import imageForm
from .models import image
# Create your views here.


def home(request):
    if request.method=="POST":
        form=imageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=imageForm()
    img=image.objects.all()
    return render(request,'home.html',{'img':img,'form':form})