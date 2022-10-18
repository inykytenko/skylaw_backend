import os 
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from django.db import models
import random
from docx2pdf import convert
from skylaw.settings import MEDIA_ROOT

class Generate_divorcement_doc:
    path_to_save = "divorcements/docs/"
    
    def get_path_foreigner(self, isForeigner):
        doc = "divorcements/templates/divorcements_template_without_foreigner.docx"
        if isForeigner:
            doc = "divorcements/templates/divorcements_template.docx"
        return doc
    
    def get_path_child(self, isDivorcementChild):
        doc = "divorcements/templates/divorcements_template_without_child.docx"
        if isDivorcementChild:
            doc = "divorcements/templates/divorcements_template.docx"
        return doc    
         
        
    # divorcement - Divorcement model
    def generate_docx(self, divorcement, dChildList):
        #  get contact info
        resolved_path = self.get_path_foreigner(divorcement.foreigner)
        doc = DocxTemplate(resolved_path)
        
        
        first_person_pass = divorcement.first_person_passport
        image_first_person_passport_pass = InlineImage(doc, first_person_pass, width=Mm(200)) # width is in millimetres
        first_person_tin_pass = divorcement.first_person_tin_file
        image_first_person_tin_pass = InlineImage(doc, first_person_tin_pass, width=Mm(200))
        first_person_residence_certificate_pass = divorcement.first_person_residence_certificate
        image_first_person_residence_certificate_pass = InlineImage(doc, first_person_residence_certificate_pass, width=Mm(200))
        copy_of_marriage_certificate_pass = divorcement.copy_of_marriage_certificate
        image_copy_of_marriage_certificate_pass = InlineImage(doc, copy_of_marriage_certificate_pass, width=Mm(200))
        
       #TODO: add a proper path
        context = {
            #першим має бути назва суду. 
            'court' : divorcement.court,
            #позивач ФІО
            'first_person_full_name' : divorcement.first_person_full_name,
            #РНОКПП
            'first_person_tin' : divorcement.first_person_tin,
            #адреса реєстрації 
            'first_person_cities' : divorcement.first_person_city,
            'first_person_street' : divorcement.first_person_street,
            #індекс 
            'first_person_zipcode' : divorcement.first_person_zipcode,
            #номер телефона)написано засоби звязку поштові, а потім телефон, може там адреса потрібна? 
            'first_person_phone_number' : divorcement.first_person_phone_number,
            #позовна заява. ПІБ відповідача
            'second_person_full_name' : divorcement.second_person_full_name,
            #РНОКПП відповідача
            'second_person_tin': divorcement.second_person_tin,
            #адреса реєстрації 
            'second_person_city' : divorcement.second_person_city,
            'second_person_street' : divorcement.second_person_street,
            #індекс 
            'second_person_zipcode' : divorcement.second_person_zipcode,
            #номер телефона)написано засоби звязку поштові, а потім телефон, може там адреса потрібна? 
            'second_person_phone_number' : divorcement.second_person_phone_number, 
            #позовна заява на розірвання шлюбу(позивач)
            'first_person_full_name' : divorcement.first_person_full_name,
            #позовна заява на розірвання шлюбу(відповідач)
            'second_person_full_name': divorcement.second_person_full_name,
            #скільки років не проживають разом(додаткові дані)
            'parting_period': divorcement.parting_period,
            #ПІБ дитини (додаткові дані)
           #якщо шлюб укладено з іноземцем
            'foreigner': divorcement.foreigner, 
            #ПРОШУ:1.   Розірватишлюб,укладений між
            #позивач ФІО
            'first_person_full_name' : divorcement.first_person_full_name,
            #ПІБ відповідача
            'second_person_full_name' : divorcement.second_person_full_name,
            #зображення
            'image_first_person_passport_pass': image_first_person_passport_pass,
            'image_first_person_tin_pass' : image_first_person_tin_pass, 
            'image_first_person_residence_certificate_pass' : image_first_person_residence_certificate_pass,
            'copy_of_marriage_certificate_pass' : image_copy_of_marriage_certificate_pass,
        }
        
        c = 0
        if dChildList:
            for child in dChildList:
                image_child_birth_certificate_pass = InlineImage(doc, child.child_birth_certificate, width=Mm(200))
                name = 'child_birth_certificate_pass_' + str(c)
                context.update({name: image_child_birth_certificate_pass})
                c += 1
 
        if dChildList:
              names = { 'child_full_name' : ', '.join(map(lambda child : child.child_full_name, dChildList))}
              context.update(names)
                            
        doc.render(context)
        pref = str(random.randint(1,10000))
 
        doc_name = ""+self.path_to_save + pref + "_" + divorcement.first_person_full_name + "_divorcement.docx"
        doc.save(doc_name)
        print(doc_name)
        return doc_name
    
    def generate_pdf(self, path_to_docx):
        # convert(path_to_docx)
        # convert(path_to_docx, "output.pdf")
        # convert("my_docx_folder/")
        return
