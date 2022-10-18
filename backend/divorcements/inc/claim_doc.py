from email.mime import application
import os 
from docxtpl import DocxTemplate
from django.db import models
import random
from docx2pdf import convert

class Claim:
    path_to_save = "divorcements/docs/"
    
    
    def generate_docx(self, divorcement):
            #  get contact info
            path = "divorcements/templates/claim_template.docx"
            doc = DocxTemplate(path)    
            

        #TODO: add a proper path ЗАЯВА про визнання позовних вимог відповідачем
            context = {
            #першим має бути назва суду.
            'court' : divorcement.court,
            #відповідач ФІО
            'second_person_full_name' : divorcement.second_person_full_name,
            #РНОКПП відповідача, якщо вказано
            'second_person_tin' : divorcement.second_person_tin,
            #індекс відповідача
            'second_person_zipcode' : divorcement.second_person_zipcode,
            #адреса реєстрації відповідача
            'second_person_cities' : divorcement.second_person_city,
            'second_person_street' : divorcement.second_person_street,
            #номер телефону відповідача, якщо вказано
            'second_person_phone_number' : divorcement.second_person_phone_number,
            #ЗАЯВА про визнання позовних вимог відповідачем
            #назва суду 
            'court' : divorcement.court,
            #відповідач ФІО
            'second_person_full_name' : divorcement.second_person_full_name,
            #позивач ФІО
            'first_person_full_name' : divorcement.first_person_full_name,
            #прошу номер справи, дані суду/немає даних
            
            # чия адреса? позивача, відповідача чи якогось органу?
            #ПІБ там де підпис, відповідача
            'second_person_full_name' : divorcement.second_person_full_name, 
            
            
        }
        
            doc.render(context)
            pref = str(random.randint(1,10000))
            doc_name = ""+self.path_to_save + pref + "_" + divorcement.second_person_full_name + "_claim_doc.docx"
            doc.save(doc_name)
            return doc_name
        
    def generate_pdf(self, path_to_docx):
            # convert(path_to_docx)
            convert(path_to_docx, "output.pdf")
            # convert("my_docx_folder/")
            return