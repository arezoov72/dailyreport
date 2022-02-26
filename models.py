from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse









# Create your models here.

        

 
#data of managers
#class managers(models.Model):
    #username=models.ForeignKey(User,on_delete=models.CASCADE,max_length=30,null=True,to_field='username')
    #fullname=models.CharField(max_length=255)
    #managerid=models.IntegerField(null=True)
    #postid=models.IntegerField(null=True)
    #class Meta:
        #permissions = [('is_manager', 'Can see employee')]
   

#data of managers and employee
class lotusemployee(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,max_length=30,null=True,to_field='username')
    fullname=models.CharField(max_length=255)
    managerid=models.IntegerField(null=True)
   
    class Meta:
        permissions = [('is_manager', 'Can see employee'),('is_employee', 'Can see self')]

#all datas   
class reportdetails(models.Model):
    
    username=models.ForeignKey(User,on_delete=models.CASCADE,max_length=30,null=True,to_field='username')
    fullname=models.CharField(max_length=255)
    Date=models.CharField(max_length=255)
    workdesc=models.TextField(null=True)
    otherwork=models.TextField(null=True)
    otherworkdesc=models.CharField(max_length=255)
    tag=models.CharField(max_length=500)
    managerid=models.ForeignKey(lotusemployee,on_delete=models.CASCADE,null=True)
    undonework = models.TextField(null=True)
    comment=models.TextField(null=True, blank=True,editable = True)
    public = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('dailyreport:edit_done',current_app='dailyreport')
    
 


         
    class Meta:
        db_table="dailyreport_reportdetails"
      


