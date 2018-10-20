"""
Исходная задача:
создать систему анализа статистики телефонных звонков.
На входе: 
- Номер телефона, имя вызываемого, дата/время, длительность звонка.
- CSV файлы ABC, DEF (https://www.rossvyaz.ru/activity/num_resurs/registerNum/) - позволяют любой номер телефона привязать к региону
- Таблица тарифов какого-либо оператора на междугородные звонки

Все исходные данные сохранить в БД, таблицы:
calls - id, user, phone, date, time, length, cost (id, пользователь, телефон, дата, время, длина звонка в минутах, цена в рублях)
abcdef - code, from, to, region (код региона, начало диапазона, окончание диапазона, регион)
tarifs - region, price (название региона, цена минуты в рублях с копейками) 
Индексы расставлять по необходимости.

На выходе - сводный отчет - по месяцам и регионам с суммарной стоимостью и длительностью звонков, с расчетом средней цены за минуту

Для заполнения исходной таблицы звонков использовать библиотеки faker, random.

Формат сдачи - один файл, отправлять через pull request. Формат имени: ГРУППА_ФАМИЛИЯ.py. Пример:
273604_Присяжный.py

Далее шаблон для начала
"""

import faker
import random
import pymysql.cursors

conn = pymysql.connect(host="localhost", user="root", password="password", db="calls", charset="utf8", cursorclass=pymysq.cursors.DictCursor)

def check_tables():
  #...
  return result #bool - есть или нет нужные таблицы

def create_tables():
  pass

def load_random_calls():
  pass

def load_csv_abc_def():
  pass

def check_region(tel): #str на входе
  #...
  return region #str

def get_calls():
  #
  return calls #list of dict {'user':..., 'phone':..., 'date':..., 'time':..., 'length':...}
  
if not check_tables():
  create_tables()
  load_random_calls()
  load_csv_abc_def()

for call in get_calls():
  region = check_region(call['phone'])
  price = get_price(region)
  #...
#...

#Итоговый отчет должен выводить таблицу - месяц, регион, сумма звонков
for month in months:
  for region in regions:
    print(month,region, summ)
