from django.db import models

class Result(models.Model):
    name = models.CharField(max_length=50)
    batch = models.CharField(max_length=50)
    percentage = models.CharField(max_length=50)
    
    imglink =  models.CharField(max_length=50,default="/static/blackprog.jpg")
    description =  models.TextField(max_length=100)


    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    description =  models.TextField(max_length=100)
    imglink =  models.CharField(max_length=50,default="/static/blackprog.jpg")


    def __str__(self):
        return self.name        


class Course(models.Model):
    name = models.CharField(max_length=50)
    description =  models.TextField(max_length=100)
    imglink =  models.CharField(max_length=50,default="/static/blank.png")


    def __str__(self):
        return self.name        
class Moment(models.Model):
    name = models.CharField(max_length=50)
    Uniqueid = models.CharField(max_length=10)
    short =  models.TextField(max_length=500)
    big =  models.TextField(max_length=5000)
    imglink =  models.CharField(max_length=500,default="/static/blank.png")
    linkforvideo =  models.CharField(max_length=500,null=True,default="None")
    linkformultiplephotos =  models.CharField(max_length=500,null=True,default="None")


    def __str__(self):
        return self.name        
class Contact(models.Model):
    name = models.CharField(max_length=50,)
    email = models.CharField(max_length=50,default=" ",)
    phone =  models.CharField(max_length=20,)
    desc =  models.TextField(max_length=200,)
    date =  models.DateField( auto_now=True,)


    def __str__(self):
        return self.name +' / '+ self.desc   
    