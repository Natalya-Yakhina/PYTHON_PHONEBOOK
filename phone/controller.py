# заключает в себе все функции

import recording # новый контакт
import searching # поиск
import view # пользовательский интерфейс
import logger #

def run():
     temp = view.choice()
     if temp == 1:
          print ('Вами выбрана операция внесения в справочник нового контакта')
          entry = recording.record() # Запись в справочник
          logger.log_to_file(entry)
          run()
     if temp == 2:
          print ('\nВами выбрана операция поиска контакта в справочнике\n' )
          entry = searching.search() # Поиск в справочнике
          logger.reading_file(entry)
          run()
     if temp == 3:
          print ('n=== ВСЕ КОНТАКТЫ ТЕЛЕФОННОГО СПРАВОЧНИКА ===\n')
          logger.read_all_file()  
          run()
     if temp == 4:
          print('\n Работа телефонного справочника окончена. Всего доброго.\n')
          