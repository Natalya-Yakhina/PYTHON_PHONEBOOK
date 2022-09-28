from datetime import datetime


import datetime
def  record():
    entry=[]
    sur_name = input('\nВведите Фамилию: ')
    entry.append(sur_name.title())
    name = input('Введите Имя: ')
    entry.append(name.title())
    telefon = input('Введите номер телефона: ')
    entry.append(telefon)
    dt = datetime.datetime.now()
    entry.insert(0,dt.strftime('%H:%M - %d.%m.%Y year'))
    print('Вами введена запись: ', entry)
    return entry