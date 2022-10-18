from django.db import models
from tabnanny import verbose

# Create your models here.
class Region(models.Model):
    title=models.CharField(verbose_name="Назва",max_length=100,null=True,blank=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Області"

class City(models.Model):
    title=models.CharField(verbose_name="Назва",max_length=100,null=True,blank=True)
    region=models.ForeignKey(Region,verbose_name="Область",on_delete=models.SET_NULL,null=True,blank=True,related_name="cities")


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Місто"
        verbose_name_plural = "Міста"
        
class Court(models.Model):
    title=models.CharField(verbose_name="Барський районний суд Вінницької області",max_length=200,null=True,blank=True)
    #Отримувач коштів
    recipient_of_money=models.CharField(verbose_name="Отримувач коштів",max_length=200,null=True,blank=True)
    #Код отримувача (код за ЄДРПОУ)	
    recipient_code_edrpou=models.IntegerField(verbose_name="Код отримувача (код за ЄДРПОУ)",blank=True,null=True)
    #Банк отримувача
    recipient_bank=models.CharField(verbose_name="Банк отримувача",max_length=100,null=True,blank=True)
    #Код банку отримувача (МФО)
    recipient_code_mfo=models.IntegerField(verbose_name="Код банку отримувача (МФО)",blank=True,null=True)
    #Рахунок отримувача
    recipient_account_number=models.CharField(verbose_name="Рахунок отримувача",max_length=100,blank=True,null=True)
    #Код класифікації доходів бюджету	
    budget_code=models.IntegerField(verbose_name="Код класифікації доходів бюджету",blank=True,null=True)
    #Призначення платежу
    purpose_of_payment=models.CharField(verbose_name="Призначення платежу",max_length=1000,null=True,blank=True)
    #посилання 
    link = models.CharField(max_length=2083, default="", unique=True)
    #сайт котрий ми скрапимо
    source = models.CharField(max_length=30, default="", blank=True, null=True)
    city=models.ForeignKey(City,on_delete=models.SET_NULL,null=True,blank=True) 

    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Судовий збір"
        verbose_name_plural = "Судовий збір"
    
    
    

