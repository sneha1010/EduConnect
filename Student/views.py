from datetime import date

from django.contrib.auth.models import User

from Teacher.models import Announcements,Exam,Class
from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def home(response):
    t1=Announcements.objects.all()
    t2=Class.objects.all()
    t3=Exam.objects.all()
    return render(response,"Student/student_home.html",{"t1":t1,"t2":t2,"t3":t3})

def chatbot(response):
    return render(response,"Student/ChatBot.html")

#def notes(response):
#   return render(response,"Student/student_home.html")

def timetable(response):
    return render(response,"Student/TimeTable.html")

def result(response):
    return render(response,"Student/Result.html")

#def about(response):
 #   return render(response,"Student/student_home.html")

def faq(response):
    return render(response,"Student/faq.html")

def logout_request(request):
    logout(request)
    return render(request,"Student/student_home.html",{})  

def about(request):
    return render(request,"Student/About.html",{})

def Notes(request):
    return render(request,"Student/Notes.html",{})

def viewallnotes(request):

    notes = Notes.objects.filter(status='accept')
    d = {'notes':notes}
    return render(request, 'student/viewallnotes.html',d)

def upload_notes(request):

    if request.method=='POST':
        b = request.POST['branch']
        s = request.POST['subject']
        n = request.FILES['notesfile']
        f = request.POST['filetype']
        d = request.POST['description']
        u = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=u,uploadingdate=date.today(),branch=b,subject=s,notesfile=n,
                                 filetype=f,description=d,status='pending')
            error="no"
        except:
            error="yes"
    return render(request,'student/upload_notes.html', locals())