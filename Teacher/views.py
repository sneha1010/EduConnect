from datetime import date

from django.conf import settings
from django.contrib.auth.models import User,Group
from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .decorator import allowed_users
from django.core.mail import send_mail, EmailMessage

from .models import *
from .forms import *
from .Sending_messages import *
# Create your views here.
def base(request):
    return render(request,"Teacher/base.html")

@allowed_users(allowed_roles=['admin','Professor'])
def home(response):
    return render(response,"Teacher/home.html")

def logout_request(request):
    logout(request)
    return render(request,"Teacher/home.html",{})

@allowed_users(allowed_roles=['admin','Professor'])
def index(response,id):
    a=Announcements.objects.get(id=id)
    return render(response,"Teacher/home.html",{})

@allowed_users(allowed_roles=['admin','Professor'])
def create_announcement(response):
    if response.method == "POST":
        form=createnewannouncement(response.POST)

        if form.is_valid():
            t=form.cleaned_data["text"]
            a=Announcements(text=t)
            a.save()
            
            if form.cleaned_data["check"]==True:
                users = Group.objects.get(name="student").user_set.all()
                for u in users:
                    rev_mail=u.email
                    email = EmailMessage(
                        'You have a new update',
                       t,
                       settings.EMAIL_HOST_USER,
                        ['iec2019111@iiita.ac.in' ],

                    )
                    email.fail_silently=False
                    email.send()
                messages.success(response,'Announcement was saved and messages are sent')
            else:
                messages.success(response,'Announcement was saved')
            return render(response,"Teacher/home.html",{})
    else:
        form=createnewannouncement()
        return render(response,"Teacher/announcement.html",{"form":form})

@allowed_users(allowed_roles=['admin','Professor'])
def create_class(response):
    if response.method == "POST":
        form=schedule_extra_class(response.POST)

        if form.is_valid():
            c1=form.cleaned_data["subject"]
            c2=form.cleaned_data["date"]
            c3=form.cleaned_data["time_start"]
            c4=form.cleaned_data["time_end"]
            c=Class(subject=c1,date=c2,time_start=c3,time_end=c4)
            c.save()
            t="You have a {0} extra class on {1} from {2} to {3}".format(str(c1),str(c2),str(c3),str(c4))
            # if form.cleaned_data["check"]==True:
            #     send_message(t)
            #     messages.success(response,'Class is scheduled and messages are sent')
            # else:
            #      messages.success(response,'Class is scheduled')
            # send_mail(
            #     "You have an update",
            #    t,
            #     'snehktl2000@gmail.com'
            #     ['snehktl2000@gmail.com'],
            #     fail_silently=False,
            # )
            return render(response,"Teacher/home.html",{"text":t})
    else:
        form=schedule_extra_class()
        return render(response,"Teacher/class.html",{"form":form})

@allowed_users(allowed_roles=['admin','Professor'])    
def create_exam(response):
    if response.method == "POST":
        form=schedule_exam(response.POST)

        if form.is_valid():
            e1=form.cleaned_data["subject"]
            e2=form.cleaned_data["date"]
            e3=form.cleaned_data["time_start"]
            e4=form.cleaned_data["time_end"]
            e=Exam(subject=e1,date=e2,time_start=e3,time_end=e4)
            e.save()
            t="You have a {0} exam on {1} from {2} to {3}".format(str(e1),str(e2),str(e3),str(e4))

            if form.cleaned_data["check"]==True:

                # email = EmailMessage(
                #     'Hello',
                #     'Body goes here',
                #     'snehaktl2000@gmail.com',
                #     ['snehaktl2000@gmail.com', ],
                #
                # )
                messages.success(response,'Exam is scheduled and messages are sent')
            else:
                 messages.success(response,'Exam is scheduled')
                 
            return render(response,"Teacher/home.html",{"text":t})
    else:
        form=schedule_exam()
        return render(response,"Teacher/exam.html",{"form":form})

#alert
