from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission

#Это определиня для полей заявок 
class CommonRequest(models.Model):
    # Определение полей вашей модели
    name = models.CharField(max_length=100)


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name



#Обработка для кабеля 
class Cable(models.Model):
    company = models.CharField(max_length=100)
    order_number = models.CharField(max_length=50)
    inclusion_date = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)  
    street = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=10) 
    contact_person = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class SalesRequest(models.Model):
    company = models.CharField(max_length=100)
    order_number = models.CharField(max_length=50)
    inclusion_date = models.DateField()
    city = models.CharField(max_length=100)  
    street = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=10) 
    contact_person = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)

    def __str__(self):
        return self.company



class Equipment(models.Model):
    # поля модели Equipment
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=100)
    responsible_person = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Форма для пользователей
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_storekeeper = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
   



class CommonRequest(models.Model):
    name = models.CharField(max_length=100)
    order_number = models.CharField(max_length=50)
    date = models.DateField()
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)

    def __str__(self):
        return self.name

 
