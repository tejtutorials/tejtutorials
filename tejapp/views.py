from django.shortcuts import render
from django.http import HttpResponse
from tejapp.models import Result
from tejapp.models import Teacher
from tejapp.models import Course
from tejapp.models import Contact
from tejapp.models import Moment
from datetime import datetime




def fac1(request):
    context = {
       'teacher' :  Teacher.objects.all()}
    return render(request,'faculty1.html',context)


def cour1(request):
    context = {
       'course' :  Course.objects.all()}
    return render(request,'courses1.html',context)





def connect1(request):
    if request.method == 'POST' :
        print(request.POST)
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        sub = request.POST.get('subject')
        desc = request.POST.get('message')
        print(name, email, phone, sub, desc)
        contact = Contact(name=name, email=email, phone=phone, desc="Subject :"+sub+" Msg:"+ desc, date=datetime.today())
        contact.save()
    return render(request,'contact1.html')



def gal1(request):
    context = {
       'moment' :  Moment.objects.all(),
       'count' :   range( Moment.objects.all().count()),
       'exactcount' :    Moment.objects.all().count()}
    return render(request,'gallery1.html',context)

def index1(request):
    context = {
       'result' :  Result.objects.all().order_by('-percentage').values(),
       'count' :   range( Result.objects.all().count())}
    print(Result.objects.all().count())
    return render(request,'index1.html',context)
