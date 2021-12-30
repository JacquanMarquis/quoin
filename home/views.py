from django.shortcuts import render, HttpResponse
from home.models import Contact

def home(request):
    #return HttpResponse("This is my Home page.")
    context = {'name': 'Harry', 'course': 'Django'}
    return render(request, 'home.html', context)

def about(request):
    #return HttpResponse("This is my About page.")
    return render(request, 'about.html')

def contact(request):
    #return HttpResponse("This is my Contact page.")
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, phone, email, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'contact.html')

def project(request):
    return HttpResponse("This is my Project page.")
    return render(request, 'project.html')


