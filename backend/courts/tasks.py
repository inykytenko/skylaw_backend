import requests
from bs4 import BeautifulSoup

from courts.models import Court

# функция скрапинга

def get_value(rows, number):
    return rows[number].find_all('td')[0].textзне

def parcing_page():
    court = {}
    try:
        print('Starting the scraping tool')
        # выполняем запрос, разбираем данные с помощью XML
        # разбираем данные в BS4
        url = 'https://brs.vn.court.gov.ua/sud0201/gromadyanam/tax/'
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        
        # выбираем из данных только "items", которые нам нужны
        table = soup.find('table', class_='table table-bordered table-striped table-condensed') 
        court_name = soup.find(id='ust_title').text
        
        rows = table.find_all('tr')
        
        court = {
            'title': court_name,
            'recipient_of_money': get_value(rows, 0),
            'recipient_code_edrpou' : get_value(rows, 1).strip('&0.'),
            'recipient_bank' : get_value(rows, 2).strip('&0.'),
            'recipient_code_mfo' : get_value(rows, 3).strip('&0.'),
            'recipient_account_number' : get_value(rows, 4),
            'budget_code' : get_value(rows, 5).strip('&0.'),
            'purpose_of_payment': get_value(rows, 6),
            'link': url,
        }
                
        print('Finished scraping')
    
            # после цикла передаем сохраненный объект в файл .txt
        return save_function(court_fee)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e) 
        
def save_function(fee):
    print('starting')
    try:
        Court.objects.create(
            title = fee['title'],
            recipient_of_money = fee['recipient_of_money'] ,
            recipient_code_edrpou = fee['recipient_code_edrpou'],
            recipient_bank = fee['recipient_bank'],
            recipient_code_mfo = fee['recipient_code_mfo'],
            recipient_account_number = fee['recipient_account_number'],
            budget_code = fee['budget_code'],
            purpose_of_payment = fee['purpose_of_payment'],
            link = fee['link'],
        )
    except Exception as e:
        print('failed at fee is none')
        print(e)
    return print('finished')        