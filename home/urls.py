from django.contrib import admin
from django.urls import path
from home import views



urlpatterns = [
    # path("",views.index,name='home'),
    # path("about",views.about,name='about'),
    # path("services",views.services,name='services'),
    # path("contact",views.contact,name='contact'),


    ##  This is for new site
    # path("newapp",views.newapp,name='newapp'),
    path("",views.newapp,name='newapp'),
    path("viewtable",views.viewtable,name='viewtable'),
    path("deletenewapp/<newapp_id>",views.deletenewapp,name='deletenewapp'),
    path("updatenewapp/<newapp_id>",views.updatenewapp,name='updatenewapp'),
    path("updatenewappfunc/<newapp_id>",views.updatenewappfunc,name='updatenewappfunc'),


    path("testsite",views.testsite,name='testsite'),
    path("addexam",views.addexam,name='addexam'),
    path("viewexam",views.viewexam,name='viewexam'),
    path("updateexam/<addexam_id>",views.updateexam,name='updateexam'),
    path("updatefunc/<addexam_id>",views.updatefunc,name='updatefunc'),
    path("deleteexam/<addexam_id>",views.deleteexam,name='deleteexam'),
    
    

]
