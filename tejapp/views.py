

from django.shortcuts import render
from django.http import HttpResponse
from tejapp.models import Result
from tejapp.models import Teacher
from tejapp.models import Course
from tejapp.models import Contact
from tejapp.models import Moment
from datetime import datetime
def index(request):
    context = {
        
    }
    return render(request,'index.html',context)
def fac(request):
    context = {
       'teacher' :  Teacher.objects.all()}
    return render(request,'faculty.html',context)
def cour(request):
    context = {
       'course' :  Course.objects.all()}
    return render(request,'courses.html',context)
def whyus(request):
    context = {
       'result' :  Result.objects.all()}
    return render(request,'whyus.html',context)
def conwu(request):
    if request.method == 'POST' :
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('message')
        # print(name,email,phon,desc)
        contact = Contact(name=name, email= email, phone=phone,desc = desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
def gal(request):
    context = {
       'moment' :  Moment.objects.all()}
    return render(request,'gallery.html',context)

