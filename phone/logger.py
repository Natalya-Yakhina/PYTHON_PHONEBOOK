# записывает инфу о выполненных операциях


from datetime import datetime
# import output

def log_to_file(entry):  
    
    with open('phone.csv', 'a') as file:
        file.write(
            f'{entry[0]};{entry[1]};{entry[2]};{entry[3]};{entry[4]};\n')

def read_all_file(): #чтение всего файла

        with open('phone.csv', 'r') as file:
            for line in file:
                print(line)