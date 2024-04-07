# импортируем необходимые библиотеки
import random
import sys
import time

# получить и подготовить данные
with open('git.txt','r',encoding='utf-8') as file:
    data=[[k.strip() for k in i.split('#')] for i in file.read().splitlines()]


# эта функция выводит в случайном порядке в одном и том же месте терминала (не сдвигаю сроки вниз) на первой строке комментарий, а на второй код
def training():
    input('Вы находитесь в тренировочном режиме, нажимайте клавишу клавесина ENTER для построчного вывода команд, если Вам надоест смотреть \nкоманды Вы всегда можете выдернуть шнур компьютера из розетки или написть - ХВАТИТ')
    print()
    while True:
        n=random.choice(data)
        comment = n[1]
        code = n[0]
        sys.stdout.write(f"{comment}\n")
        sys.stdout.write(f"{code}\n")
        # sys.stdout.flush() программа должна работать без этой команды - проверить
        if input()=='ХВАТИТ':
            break
        sys.stdout.write('\033[F' * 3)  # Возврат курсора на три строки назад
        sys.stdout.write(f" {len(comment)*' '}\n")  
        sys.stdout.write(f" {len(code)*' '}\n")
        sys.stdout.write('\033[F' * 2)


def battle():
    input('''Вы находитесь в боевом режиме, нажмите клавишу клавесина ENTER, берите в руки клавиатуру и гребите к берегу,
и пусть вам повезет в бесконечном цикле. Если все надоест напишите - ХВАТИТ ''')
    print()
    while True:
        n=random.choice(data)
        comment = n[1]
        code = n[0]
        sys.stdout.write(f"{comment}\n")
        sys.stdout.write(f"{code}\r")
        int=input()
        if int=='ХВАТИТ':
            break
        if int==code:
            sys.stdout.write('\033[F' * 2)  # Возврат курсора на две строки назад
            sys.stdout.write(f" {len(comment)*' '}\n")  
            sys.stdout.write(f" {len(code)*' '}\n")
            sys.stdout.write('\033[F' * 2)
        else:
            while True:
                sys.stdout.write('\033[F' * 2)  # Возврат курсора на две строки назад
                sys.stdout.write(f" {len(comment)*' '}\n")  
                sys.stdout.write(f" {len(code)*' '}\n")
                sys.stdout.write('\033[F' * 2)
                sys.stdout.write(f"{comment}\n")
                sys.stdout.write(f"{code}\r")
                int=input()
                if int==code:
                    break
                if int=='ХВАТИТ':
                    break



battle()

 
        




    





    
    

    
        
