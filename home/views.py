from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# This is for new site
from home.models import Newapp
from hello.filters import ViewtableFilter
from home.models import Addexam
from home.models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def index(request):
    # return HttpResponse('This is homepage')
    context = {
        'variable': "this is from views"
    }

    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request, "contact.html")


# This is for new site
def newapp(request):
    if request.method == "POST":
        newappname = request.POST.get('newappname')
        newappemail = request.POST.get('newappemail')
        newappphone = request.POST.get('newappphone')
        newappaddress = request.POST.get('newappaddress')
        newappdepart = request.POST.get('newappdepart')
        newappposition=request.POST.get('newappposition')
        newapp = Newapp(newappname=newappname, newappemail=newappemail,
                        newappphone=newappphone, newappaddress=newappaddress, newappdepart=newappdepart,
                        newappposition=newappposition)
        newapp.save()
        messages.success(request, 'Saved')
    return render(request, "newapp.html")


def viewtable(request):
    newapp_data = Newapp.objects.all()
    # This is for filter upto 5 min
    viewfilter = ViewtableFilter(request.GET, queryset=newapp_data)
    newapp_data = viewfilter.qs
    data = {
        "newapp_data": newapp_data,
        'viewfilter': viewfilter
    }
    return render(request, "viewtable.html", data)

def updatenewapp(request, newapp_id):
    newapp_data = Newapp.objects.get(pk=newapp_id)
    allnewapp_data = Newapp.objects.all()
    data = {
        'allnewapp_data': allnewapp_data,
        'newapp_data': newapp_data,

    }

    return render(request, "newapp.html", data)


def updatenewappfunc(request, newapp_id):
    newapp_data = Newapp.objects.get(pk=newapp_id)
    newapp_data.newappname = request.POST.get('newappname')
    newapp_data.newappemail = request.POST.get('newappemail')
    newapp_data.newappphone = request.POST.get('newappphone')
    newapp_data.newappaddress = request.POST.get('newappaddress')
    newapp_data.newappdepart = request.POST.get('newappdepart')
    newapp_data.newappposition = request.POST.get('newappposition')
    newapp_data.save()
    messages.success(request, 'Invigilator updated')
    return redirect('viewtable')




def deletenewapp(request, newapp_id):
    newapp_data = Newapp.objects.get(pk=newapp_id)
    newapp_data.delete()
    messages.success(request, 'Invisilator deleted')
    return redirect('viewtable')

def testsite(request):
    return render(request, "testsite.html")


def addexam(request):
    if request.method == "POST":
        examname = request.POST.get('examname')
        examtype = request.POST.get('examtype')
        examsemtype = request.POST.get('examsemtype')
        regularback = request.POST.get('regularback')
        examcentre = request.POST.get('examcentre')
        examdate = request.POST.get('examdate')
        newexamdate = request.POST.get('examdate')
        examtime = request.POST.get('examtime')
        newexamtime = request.POST.get('examtime')
        examdesc = request.POST.get('examdesc')

        addexam = Addexam(examname=examname, examtype=examtype, examsemtype=examsemtype,
                          regularback=regularback, examcentre=examcentre, examdate=examdate,
                          newexamdate=newexamdate,examtime=examtime,newexamtime=newexamtime ,examdesc=examdesc)
        addexam.save()
        messages.success(request, 'Exam added')
    return render(request, "addexam.html")


def viewexam(request):
    addexam_data = Addexam.objects.all()
    

    exam_data = {
        "addexam_data": addexam_data,
        
        
    }
    return render(request, "viewexam.html", exam_data)



def updateexam(request, addexam_id):
    addexam_data = Addexam.objects.get(pk=addexam_id)
    

    buildingsinexam=addexam_data.examaddbuilding.all()
    removedbuildingsinexam_data = Addbuilding.objects.exclude(pk__in=buildingsinexam)
    alladdbuilding_data = Addbuilding.objects.all()

    allexam_data = Addexam.objects.all()
    
    # filternewapp_data = Newapp.objects.all()
    

    data = {
        'allexam_data': allexam_data,
        'addexam_data': addexam_data,
        
        
        'buildingsinexam':buildingsinexam,
        'removedbuildingsinexam_data':removedbuildingsinexam_data,
        'alladdbuilding_data':alladdbuilding_data,

    }

    return render(request, "addexam.html", data)


def updatefunc(request, addexam_id):
    addexam_data = Addexam.objects.get(pk=addexam_id)
    addexam_data.examname = request.POST.get('examname')
    addexam_data.examtype = request.POST.get('examtype')
    addexam_data.examsemtype = request.POST.get('examsemtype')
    addexam_data.regularback = request.POST.get('regularback')
    addexam_data.examcentre = request.POST.get('examcentre')
    addexam_data.examdate = request.POST.get('examdate')
    addexam_data.newexamdate = request.POST.get('examdate')
    addexam_data.examtime = request.POST.get('examtime')
    addexam_data.newexamtime = request.POST.get('examtime')
    addexam_data.examdesc = request.POST.get('examdesc')
    addexam_data.save()
    messages.success(request, 'Exam updated')
    return redirect('viewexam')

def deleteexam(request, addexam_id):
    addexam_data = Addexam.objects.get(pk=addexam_id)
    addexam_data.delete()
    messages.success(request, 'Exam deleted')
    return redirect('viewexam')

def addinvigilator(request,newapp_id, addexam_id):
    addexam_data = Addexam.objects.get(pk=addexam_id)
    newapp_data=Newapp.objects.get(pk=newapp_id)
    addexam_data.examnewapp.add(newapp_data)
    
    return redirect('updateexam',addexam_id)

def deleteinvigilator(request,newapp_id, addexam_id):
    addexam_data = Addexam.objects.get(pk=addexam_id)
    newapp_data=Newapp.objects.get(pk=newapp_id)
    addexam_data.examnewapp.remove(newapp_data)    
    return redirect('updateexam',addexam_id)
    if request.method == "POST":
        roomname = request.POST.get('roomname')
        addroom = Addroom(roomname=roomname)
        addroom.save()
        messages.success(request, 'Room added')
    allroom_data = Addroom.objects.all()
    data={
        'allroom_data':allroom_data,
    }
    return render(request, "addroom.html",data)

def addroom(request):
    if request.method == "POST":
        roomname = request.POST.get('roomname')
        addroom = Addroom(roomname=roomname)
        addroom.save()
        messages.success(request, 'Room added')
    allroom_data = Addroom.objects.all()
    data={
        'allroom_data':allroom_data,
    }
    return render(request, "addroom.html",data)

def deleteroom(request, addroom_id):
    addroom_data = Addroom.objects.get(pk=addroom_id)
    addroom_data.delete()
    messages.success(request, 'Room deleted')
    return redirect('addroom')


def updateroom(request, addroom_id):
    addroom_data = Addroom.objects.get(pk=addroom_id)
    allroom_data = Addroom.objects.all()

    teachers=addroom_data.invigilatorsinroom.all()
    removednewapp_data = Newapp.objects.exclude(pk__in=teachers)
    allnewapp_data = Newapp.objects.all()
    # filternewapp_data = Newapp.objects.all()
    viewfilter = ViewtableFilter(request.GET, queryset=removednewapp_data)
    removednewapp_data = viewfilter.qs
    data = {
        'allroom_data': allroom_data,
        'addroom_data': addroom_data,
        'teachers':teachers,
        'allnewapp_data':allnewapp_data,
        'removednewapp_data':removednewapp_data,
        'viewfilter':viewfilter,
    }

    return render(request, "addroom.html", data)


def updateroomfunc(request, addroom_id):
    addroom_data = Addroom.objects.get(pk=addroom_id)
    addroom_data.roomname = request.POST.get('roomname')
    
    addroom_data.save()
    messages.success(request, 'Room updated')
    return redirect('addroom')

def addinvigilatorinroom(request,newapp_id, addroom_id):
    addroom_data = Addroom.objects.get(pk=addroom_id)
    newapp_data=Newapp.objects.get(pk=newapp_id)
    addroom_data.invigilatorsinroom.add(newapp_data)
    
    return redirect('updateroom',addroom_id)

def deleteinvigilatorfromroom(request,newapp_id, addroom_id):

    addroom_data = Addroom.objects.get(pk=addroom_id)
    newapp_data=Newapp.objects.get(pk=newapp_id)
    addroom_data.invigilatorsinroom.remove(newapp_data)
    return redirect('updateroom',addroom_id)



def addbuilding(request):
    if request.method == "POST":
        buildingname = request.POST.get('buildingname')
        addbuilding = Addbuilding(buildingname=buildingname)
        addbuilding.save()
        messages.success(request, 'Building added')
    allbuilding_data = Addbuilding.objects.all()
    data={
        'allbuilding_data':allbuilding_data,
    }
    return render(request, "addbuilding.html",data)


def testsite(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        testing = Testing(name=name)
        testing.save()
        messages.success(request, 'Test data sent')
    alltest_data = Testing.objects.all()
    allnewapp_data = Newapp.objects.all()
    alladdexam_data = Addexam.objects.all()
    data={
        'alltest_data':alltest_data,
        'allnewapp_data':allnewapp_data,
        'alladdexam_data':alladdexam_data,
    }
    return render(request, "testsite.html",data)



def deletebuilding(request, addbuilding_id):
    addbuilding_data = Addbuilding.objects.get(pk=addbuilding_id)
    addbuilding_data.delete()
    messages.success(request, 'Building deleted')
    return redirect('addbuilding')

def updatebuilding(request, addbuilding_id):
    
    addbuilding_data = Addbuilding.objects.get(pk=addbuilding_id)
    allbuilding_data = Addbuilding.objects.all()

    roomsinbuilding=addbuilding_data.rooms.all()
    removedroom_data = Addroom.objects.exclude(pk__in=roomsinbuilding)
    allroom_data = Addroom.objects.all()
    data = {
        'addbuilding_data': addbuilding_data,
        'allbuilding_data': allbuilding_data,
        'roomsinbuilding':roomsinbuilding,
        'removedroom_data':removedroom_data,
        'allroom_data':allroom_data,
        
    }
    return render(request, "addbuilding.html", data)


def updatebuildingfunc(request, addbuilding_id):
    
    addbuilding_data = Addbuilding.objects.get(pk=addbuilding_id)
    addbuilding_data.buildingname = request.POST.get('buildingname')
    
    addbuilding_data.save()
    messages.success(request, 'Building updated')
    return redirect('addbuilding')


def deleteroomfrombuilding(request,addroom_id, addbuilding_id):

    addbuilding_data=Addbuilding.objects.get(pk=addbuilding_id)
    addroom_data = Addroom.objects.get(pk=addroom_id)
    
    addbuilding_data.rooms.remove(addroom_data)
    return redirect('updatebuilding',addbuilding_id)

def addroominbuilding(request,addroom_id, addbuilding_id):
    addbuilding_data=Addbuilding.objects.get(pk=addbuilding_id)
    addroom_data = Addroom.objects.get(pk=addroom_id)
    
    addbuilding_data.rooms.add(addroom_data)
    return redirect('updatebuilding',addbuilding_id)

def deletebuildingfromexam(request,addbuilding_id, addexam_id):

    addbuilding_data=Addbuilding.objects.get(pk=addbuilding_id)
    addexam_data = Addexam.objects.get(pk=addexam_id)
    
    addexam_data.examaddbuilding.remove(addbuilding_data)
    return redirect('updateexam',addexam_id)


def addbuildinginexam(request,addbuilding_id, addexam_id):
    addbuilding_data=Addbuilding.objects.get(pk=addbuilding_id)
    addexam_data = Addexam.objects.get(pk=addexam_id)
    
    addexam_data.examaddbuilding.add(addbuilding_data)
    return redirect('updateexam',addexam_id)


def handleSignup(request):
    if request.method=="POST":
        signupusername=request.POST['signupusername']
        signuppassword1=request.POST['signuppassword1']
        signuppassword2=request.POST['signuppassword2']

        if not signupusername.isalnum():
            

            messages.error(request,"Username should only contain letter and number")
            return redirect('/')

        if signuppassword1!=signuppassword2:
            messages.error(request,"Passwords do not match")
            return redirect('/')
        myuser=User.objects.create_user(signupusername,None,signuppassword1)
        myuser.save()
        messages.success(request,"Account successfully created")

        return redirect('/')

        
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword1=request.POST['loginpassword1']
        
        user=authenticate(username=loginusername,password=loginpassword1)

        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully logged in')
            return redirect('/')
        else:
            messages.error(request, 'Unsuccessfull to log in, Please try again')
            return redirect('/')
    return HttpResponse('404 - Not Found')

def handleLogout(request):
    
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('/')
    

