from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login
from datetime import date
# Create your views here.

def about(request):
    return render(request,'notes/about.html')

def index(request):
    return render(request,'notes/index.html')


def userlogin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'notes/login.html', locals())

def login_admin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error ="yes"
        except:
            error = "yes"
    return render(request,'notes/login_admin.html', locals())


def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    pn = Notes.objects.filter(status="pending").count()
    an = Notes.objects.filter(status="Accept").count()
    rn = Notes.objects.filter(status="Reject").count()
    alln = Notes.objects.all().count()
    d = {'pn':pn,'an':an,'rn':rn,'alln':alln}
    return render(request,'notes/admin_home.html',d)








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
    return render(request,'notes/upload_notes.html', locals())

def view_mynotes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(user = user)

    d = {'notes':notes}
    return render(request,'notes/view_mynotes.html',d)

def delete_mynotes(request,pid):
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('view_mynotes')

def view_allnotes(request):

    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(user = user)

    d = {'notes':notes}
    return render(request,'notes/view_allnotes.html',d)



def delete_users(request,pid):

    user = User.objects.get(id=pid)
    user.delete()
    return redirect('notes/view_users')

def pending_notes(request):

    notes = Notes.objects.filter(status = "pending")
    d = {'notes':notes}
    return render(request, 'notes/pending_notes.html',d)

def accepted_notes(request):

    notes = Notes.objects.filter(status = "Accept")
    d = {'notes':notes}
    return render(request, 'notes/accepted_notes.html',d)

def rejected_notes(request):

    notes = Notes.objects.filter(status = "Reject")
    d = {'notes':notes}
    return render(request, 'notes/rejected_notes.html',d)

def all_notes(request):

    notes = Notes.objects.all()
    d = {'notes':notes}
    return render(request, 'notes/all_notes.html',d)

def assign_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.get(id=pid)
    error = ""
    if request.method=='POST':
        s = request.POST['status']
        try:
            notes.status = s
            notes.save()
            error="no"
        except:
            error="yes"
    d = {'notes':notes,'error':error}
    return render(request, 'notes/assign_status.html',d)

def delete_notes(request,pid):
    # if not request.user.is_authenticated:
    #     return redirect('login')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    notes = Notes.objects.filter(status='pending')
    d = {'notes': notes}
    return  redirect('notes/viewallnotes.html',d)

def viewallnotes(request):

    notes = Notes.objects.filter(status='accept')
    d = {'notes':notes}
    return render(request, 'notes/viewallnotes.html',d)

