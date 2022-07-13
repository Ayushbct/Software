from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# This is for new site
from home.models import Newapp
from hello.filters import ViewtableFilter
from home.models import Addexam

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
        newapp = Newapp(newappname=newappname, newappemail=newappemail,
                        newappphone=newappphone, newappaddress=newappaddress, newappdepart=newappdepart)
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
    newapp_data.save()
    messages.success(request, 'Invisilator updated')
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
    teachers=addexam_data.examnewapp.all()
    allexam_data = Addexam.objects.all()
    data = {
        'allexam_data': allexam_data,
        'addexam_data': addexam_data,
        'teachers':teachers,
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