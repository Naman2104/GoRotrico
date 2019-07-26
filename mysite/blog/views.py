from django.shortcuts import render
from .models import Blogpost, Contact
# Create your views here.
from django.http import HttpResponse


# Create your views here.
def index (request):
    myposts= Blogpost.objects.all()
    return render(request,'blog/index.html',{'myposts':myposts})

def blogpost (request,id):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request,'blog/blogpost.html',{'post':post})

def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        des = request.POST.get('des', '')
        contact = Contact(name=name, email=email, phone=phone, des=des)
        contact.save()
        thank = True
    return render(request, 'blog/contact.html', {'thank': thank})