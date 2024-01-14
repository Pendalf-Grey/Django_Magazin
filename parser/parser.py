from bs4 import BeautifulSoup
import requests
import json

'''URL Elema'''
# url = 'https://elema.by/catalog/palto-muzhskie/'

'''Делаем хэдэрс для имитации юзера, который сам делает запросы'''
# headers = {
#     'Accept': '*/*',
#     'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
# }

'''Записываем в переменную req работу с библиотекой requests'''
# req = requests.get(url, headers=headers)

'''Делаем текстовый файл из req и записываем в переменную src'''
# src = req.text
# print(src)

'''После того как закомментили всё сверху - 
создаём файл index.html, в который закидываем HTML со страницы'''
with open('index.html', encoding='utf-8') as file:
    src = file.read()


soup = BeautifulSoup(src, 'lxml')

'''Ищем через класс все ссылки на пальто'''
link_palto = soup.find_all(class_='g-pos-abs g-height-100x g-width-100x g-z-index-2')

all_categories_dict = {}

'''Пробегаемся циклом по всем найденным данным'''
for item in link_palto:

    '''Записываем в переменную, добавлям начальный путь, отбираем все имена href'''
    item_url = 'https://elema.by' + item.get('href')

    '''Записываем в переменную текст'''
    item_text = item.text

    '''Приводим в читаемый вид данные'''
    all_categories_dict[item_text]: item_url

'''Создаём файл и закидываем туда данные в JSON-формате '''
with open('all_categories_dict.json', 'w') as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

    # print(f'{item_text}: {item_url}')
