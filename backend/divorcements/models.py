import email
from email.mime import image
from tabnanny import verbose
from types import CoroutineType
from django.db import models
from random import  choices
import string
from courts.models import Court
from courts.models import City
from divorcements.inc.generate_divorcement_doc import Generate_divorcement_doc
from divorcements.inc.claim_doc import Claim
from divorcements.inc.application_for_issuance_doc import Application_for_issuance_doc
from divorcements.inc.application_without_participation_doc import Application_without_participation
from django import forms
from skylaw.settings import MEDIA_ROOT

# Create your models here.

class Divorcement(models.Model):
    step_1=models.BooleanField(verbose_name="Перший крок",null=True,blank=True)
    step_2=models.BooleanField(verbose_name="Другий крок",null=True,blank=True)
    step_3=models.BooleanField(verbose_name="Третій крок",null=True,blank=True)
    step_4=models.BooleanField(verbose_name="Четвертий крок",null=True,blank=True)
    step_5=models.BooleanField(verbose_name="П'ятий крок",null=True,blank=True)
    token = models.CharField(verbose_name="Токен",max_length=16,null=True,blank=True)
    #step1
    # (Дані першої особи)
    first_person_phone_number=models.CharField(verbose_name="Номер телефона",max_length=13,null=True,blank=True)
    first_person_full_name=models.CharField(max_length=100,verbose_name="Ваше ПІБ",blank=True,null=True)
    first_person_tin=models.IntegerField(verbose_name="РНОКПП",blank=True,null=True)
    first_person_zipcode=models.IntegerField(verbose_name="індекс",blank=True,null=True)
    #first_person_region
    first_person_city=models.ForeignKey(City,verbose_name="Місто",on_delete=models.SET_NULL,null=True,blank=True,related_name="first_person_cities")
    first_person_street=models.CharField(max_length=100,verbose_name="Вулиця",blank=True,null=True)
    first_person_passport=models.FileField(verbose_name="Фото паспорта",null=True,blank=True,upload_to= 'images/')
    first_person_tin_file=models.FileField(verbose_name="Фото РНОКПП",blank=True,null=True,upload_to='images/')
    first_person_residence_certificate=models.FileField(verbose_name="Фото довідки про адресу",blank=True,null=True,upload_to='images/')
    #step2
    # (Дані другої особи(чоловіка/дружини))
    second_person_full_name = models.CharField(max_length=100,verbose_name="ПІБ чоловіка/дружини",blank=True,null=True)
    second_person_tin=models.IntegerField(verbose_name="РНОКПП чоловіка/дружини",blank=True,null=True)
    second_person_zipcode=models.IntegerField(verbose_name="індекс",blank=True,null=True)
    second_person_phone_number=models.CharField(verbose_name="Номер телефона",max_length=13,null=True,blank=True)
    #second_person_region
    second_person_city=models.ForeignKey(City,verbose_name="Місто",on_delete=models.SET_NULL,null=True,blank=True,related_name="second_person_cities")
    second_person_street=models.CharField(verbose_name="Вулиця чоловіка/дружини",max_length=100,blank=True,null=True)
    maiden_name=models.CharField(verbose_name="Дівоче прізвище",max_length=50,blank=True,null=True)
    parting_period=models.CharField(verbose_name="Cрок протягом якого не проживаємо разом",max_length=10,null=True,blank=True)

    foreigner=models.BooleanField(verbose_name="Іноземець",null=True,blank=True)
    copy_of_marriage_certificate= models.FileField(verbose_name="Фото копії свідотцтва про шлюб",blank=True,null=True,upload_to='images/')
    court=models.ForeignKey(Court,on_delete=models.SET_NULL,null=True,blank=True) 

    #step3
    
    #(step4 Оплата послуг та судового збору)
    is_paid=models.BooleanField(verbose_name="Оплата",null=True,blank=True)

    #step5
    #(Отримання документу)
    email=models.EmailField(verbose_name="Електрона пошта",blank=True,null=True)

    #step6
    #(Відгук)
    response=models.TextField(verbose_name="Відгук",blank=True,null=True)
    court_city=models.ForeignKey(City,verbose_name="Місто",on_delete=models.SET_NULL,null=True,blank=True,related_name="court_cities")

    def __str__(self):
        return self.token        

    def save(self, *args, **kwargs):
        if not self.token:
            while(True):
                token = ''.join(choices(string.ascii_letters + string.digits, k=16))
                divorcements = Divorcement.objects.filter(token=token)
                if divorcements.count():
                    continue
                self.token = token
                break
                   
            
        #need check if already exists?
        #ЗАЯВА про розірвання шлюбу
        #generate divorcement doc
        gdd = Generate_divorcement_doc()
        
        # find child by divorcement
        # array[child]
        children = DivorcementChild.objects.filter(divorcement=self)
        
        doc_path = gdd.generate_docx(self, children)
        gdd.generate_pdf(doc_path)
        #ЗАЯВА про визнання позовних вимог відповідачем
        #generate claim
        gcd = Claim()
        doc_path = gcd.generate_docx(self)
        gcd.generate_pdf(doc_path)
        #ЗАЯВА про розгляд справи без участі
        #gawithout - generate Application_without_participation
        gawithout = Application_without_participation()
        doc_path = gawithout.generate_docx(self)
        gawithout.generate_pdf(doc_path)
        #ЗАЯВА про видачу копії судового рішення 
        #gafor - generation Application_for_issuance_doc
        gafor = Application_for_issuance_doc()
        doc_path = gafor.generate_docx(self)
        gafor.generate_pdf(doc_path)
        

        super().save(*args, **kwargs)
    

    class Meta:
        verbose_name = "Розлучення"
        verbose_name_plural = "Розлучення"


class DivorcementChild(models.Model):
    #(дані про дитину)
   child_full_name=models.CharField(max_length=100,verbose_name="ПІБ дитини",blank=True,null=True)
   child_birthday=models.DateField(verbose_name="День народження дитини",blank=True,null=True)
   child_birth_certificate=models.FileField(verbose_name="Фото свідотцва про народження дитини",blank=True,null=True,upload_to='images/')
   divorcement=models.ForeignKey(Divorcement,on_delete=models.SET_NULL,null=True,blank=True) #,related_name="child_birthday"
   
   def __str__(self):
        return self.child_full_name

   def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        
   class Meta:
        verbose_name = "Дитина"
        verbose_name_plural = "Діти"
    
    
#class DivorcementForm(forms.ModelForm):
  #  """Form for the Divorcement model"""
   # class Meta:
   #     model = Divorcement
    #    fields = ('token', 'first_person_passport', 'first_person_tin_file','first_person_residence_certificate' ) 
    
#def save_court_name(divorcement, *args, **kwargs):
 #   court_name = Divorcement.objects.filter(court_city=court).first()
 #   if court_name:
  #      divorcement = Divorcement.objects.filter(court_city=court)
  #  else:    