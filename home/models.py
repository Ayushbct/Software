from django.db import models

#This is added later
from datetime import date
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name +" : "+ self.email


class Newapp(models.Model):
    newappname=models.CharField(max_length=122)
    newappemail=models.CharField(max_length=122)
    newappphone=models.CharField(max_length=12)
    newappaddress=models.CharField(max_length=122)
    newappdepart=models.CharField(max_length=255)
    newappposition=models.CharField(max_length=255)
    
    #newappdate=models.DateField()
    def __str__(self):
        return self.newappname +" : "+ self.newappdepart

class Addexam(models.Model):
    examname=models.CharField(max_length=122)
    examtype=models.CharField(max_length=122)
    examsemtype=models.CharField(max_length=122,blank=True,null=True)
    regularback=models.CharField(max_length=122,blank=True,null=True)
    examcentre=models.CharField(max_length=122)
    examdate=models.CharField(max_length=122)
    newexamdate=models.DateField(max_length=122,blank=True, null=True)
    examtime=models.CharField(max_length=122)
    newexamtime=models.TimeField(max_length=122,blank=True, null=True)
    examdesc=models.TextField()
    #examnewapp=models.ForeignKey(Newapp,blank=True,null=True, on_delete=models.CASCADE)
    examnewapp=models.ManyToManyField(Newapp,blank=True)
    def __str__(self):
        return self.examname +" : "+ self.examcentre

class Addroom(models.Model):
    roomname=models.CharField(max_length=122)
    invigilatorsinroom=models.ManyToManyField(Newapp,blank=True)
    
    def __str__(self):
        return self.roomname

class Addbuilding(models.Model):
    buildingname=models.CharField(max_length=122)
    rooms=models.ManyToManyField(Addroom,blank=True)
    
    def __str__(self):
        return self.buildingname

class Testing(models.Model):
    name=models.CharField(max_length=122)
    def __str__(self):
        return self.name
