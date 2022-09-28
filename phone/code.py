# import time
# import string
# import secrets

# print()
# print("ТЕЛЕФОННЫЙ СПРАВОЧНИК")

# # создание файла 
# filename = "Tel_book.csv" 
# myfile = open(filename, "a+") 
# myfile.close
 
# # метод главного меню 
# def main_menu(): 
#     print( "\nГЛАВНОЕ МЕНЮ\n") 
#     print( "1. Просмотреть все контакты") 
#     print( "2. Добавить новый контакт") 
#     print( "3. Поиск контактов") 
#     print( "4. Выход") 
#     choice = input("Выберите пункт меню: ") 
#     if choice == "1": 
#         myfile = open(filename, "r+") 
#         filecontents = myfile.read() 
#         if len(filecontents) == 0: 
#             print( "Искомый контакт не обнаружен, печаль-тоска") 
#         else: 
#             print(filecontents) 
#         myfile.close 
#         enter = input("Для продолжения нажмите Enter") 
#         main_menu() 
#     elif choice == "2": 
#         newcontact() 
#         enter = input("Для продолжения нажмите Enter") 
#         main_menu() 
#     elif choice == "3": 
#         searchcontact() 
#         enter = input("Для продолжения нажмите Enter") 
#         main_menu() 
#     elif choice == "4": 
#         print("Спасибо, что тыкаете пальчиками тут всякое.") 
#     else: 
#         print( "Пожалуйста, повторите ввод\n") 
#         enter = input("Для продолжения нажмите Enter")
#         main_menu()

# # def execute_command(command):
# #     global contacts_list
# #     if command == 1:  # Показать список контактов
# #         show_list.show_contacts(contacts_list)
# #     elif command == 2:  # Добавить контакт
# #         contacts_list = add_contact.add_contact(contacts_list)
# #     elif command == 3:  # Редактировать контакт
# #         contacts_list = edit_contact.edit_contact(contacts_list)
# #     elif command == 4:  # Удаление контакта
# #         contacts_list = delete_contact.delete(contacts_list)
# #     elif command == 5:  # Импорт из файла
# #         imported_contacts = import_from_file.import_format()
# #         if imported_contacts is not None:
# #             contacts_list += imported_contacts
# #     elif command == 6:  # Экспорт в файл
# #         export_to_file.export_format(contacts_list)
# #     else:
# #         print("Введите верную команду")









 
# # метод поиска         
# def searchcontact(): 
#     searchname = input("Введите ИМЯ для поиска контакта: ") 
#     remname = searchname[1:] 
#     firstchar = searchname[0] 
#     searchname = firstchar.upper() + remname 
#     myfile = open(filename, "r+") 
#     filecontents = myfile.readlines() 
      
#     found = False 
#     for line in filecontents: 
#         if searchname in line: 
#             print("По вашему запросу найден контакт: ", end = " ") 
#             print( line) 
#             found = True 
#             break 
#     if found == False: 
#         print(f"Контакт {searchname} не найден в справочнике, сожалею") 
 
# # имя 
# def input_firstname(): 
#     first = input("Введите ваше имя: ") 
#     remfname = first[1:] 
#     firstchar = first[0] 
#     return firstchar.upper() + remfname 
 
# # фамилия 
# def input_lastname(): 
#     last = input("Введите вашу фамилию: ") 
#     remlname = last[1:] 
#     firstchar = last[0] 
#     return firstchar.upper() + remlname

# # метод генерации ключа
# def key_gen():
#     alphabet = string.ascii_letters + string.digits
#     key = ''.join(secrets.choice(alphabet) for i in range(4))
#     return key
# key = key_gen()
 
# # сохранение новых данных контакта 
# def newcontact(): 
#     firstname = input_firstname() 
#     lastname = input_lastname() 
#     phoneNum = input("Введите ваш номер телефона: ") 
#     emailID = input("Введите ваш E-mail: ") 
#     contactDetails =(f"{key}; " + firstname + " " + lastname + "; " + phoneNum + "; " + emailID +  "\n") 
#     myfile = open(filename, "a") 
#     myfile.write(contactDetails) 
#     print("Новая запись в телефонном справочнике: \n " + contactDetails + " успешно создана!")  
 
# main_menu()
# time.sleep(5)