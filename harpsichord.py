# импортируем необходимые библиотеки
import random
import sys

# получить и подготовить данные
with open('git.txt','r',encoding='utf-8') as file:
    data=[[k.strip() for k in i.split('#')] for i in file.read().splitlines()]


# вывести на экран построчно весь список команд использую клвишу ENTER
input('Нажимайте клавишу клавесина ENTER для построчного вывода команд, если Вам надоест смотреть \nкоманды Вы всегда можете выдернуть шнур компьютера из розетки или написть - ХВАТИТ')

while True:
    n=random.choice(data)
    print()
    print(n[1])
    print(n[0],end='\r')
    
    if input()=='ХВАТИТ':
        break
   


    



 
        




    





    
    

    
        
