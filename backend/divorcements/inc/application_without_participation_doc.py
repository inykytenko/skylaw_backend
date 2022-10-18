from email.mime import application
import os 
from docxtpl import DocxTemplate
from django.db import models
import random
from docx2pdf import convert

class Application_without_participation:
    path_to_save = "divorcements/docs/"
    
    def generate_docx(self, divorcement):
        #  get contact info
        path = "divorcements/templates/application_without_participation_template.docx"
        doc = DocxTemplate(path)    
    
    
    #TODO: add a proper path ЗАЯВА про розгляд справи без участі 
        context = {
        #назва суду
        'court' : divorcement.court,
        #позивач ФІО
        'first_person_full_name' : divorcement.first_person_full_name,
        #РНОКПП позивач
        'first_person_tin' : divorcement.first_person_tin,
        #індекс позивач
        'first_person_zipcode' : divorcement.first_person_zipcode,
        #адреса реєстрації позивача
        'first_person_cities' : divorcement.first_person_city,
        'first_person_street' : divorcement.first_person_street,
        #номер телефону позивача
        'first_person_phone_number' : divorcement.first_person_phone_number,
        #назва суду 
        'court' : divorcement.court,
        #позивач ФІО
        'first_person_full_name' : divorcement.first_person_full_name,
        #відповідач ФІО
        'second_person_full_name' : divorcement.second_person_full_name,
        #Розглянути справу за моїм позовом розглядати за наявними в матеріалах справи документами
        #позивач ФІО там де підпис
        'first_person_full_name' : divorcement.first_person_full_name,
    }
    
        doc.render(context)
        pref = str(random.randint(1,10000))
        doc_name = ""+self.path_to_save + pref + "_" + divorcement.first_person_full_name + "_application_without_participation.docx"
        doc.save(doc_name)
        return doc_name
    
    def generate_pdf(self, path_to_docx):
        # convert(path_to_docx)
        convert(path_to_docx, "output.pdf")
        # convert("my_docx_folder/")
        return