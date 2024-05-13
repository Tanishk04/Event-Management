from django.db import models
class UserInfo1(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    mail=models.EmailField()
    address=models.CharField(max_length=200)
    phoneno=models.IntegerField()
class Event(models.Model):
    eventId=models.IntegerField()
    eventName=models.CharField(max_length=50)
    eventDateTime=models.DateTimeField()
    venue=models.CharField(max_length=100)
    desc=models.CharField(max_length=200)
class Admin(models.Model):
    adminId=models.IntegerField()
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
class Booking(models.Model):
    bookingId=models.IntegerField()
    userId=models.IntegerField()
    eventId=models.IntegerField()
    bookingTime=models.DateTimeField()
    status=models.CharField(max_length=200)
class Hall(models.Model):
    hallId=models.IntegerField()
    hallName=models.CharField(max_length=50)
    capacity=models.IntegerField()
    availability=models.BooleanField()
class Notification(models.Model):
    notificationId=models.IntegerField()
    userId=models.IntegerField()
    msg=models.CharField(max_length=200)
    sendTime=models.DateTimeField()
