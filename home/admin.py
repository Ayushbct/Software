from django.contrib import admin
from home.models import Contact
#This is for new site
from home.models import Newapp
from home.models import Addexam
# Register your models here.
admin.site.register(Contact)


#This is for new site
admin.site.register(Newapp)
admin.site.register(Addexam)