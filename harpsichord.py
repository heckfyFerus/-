with open('git.txt','r',encoding='utf-8') as file:
    data=[[k.strip() for k in i.split('#')] for i in file.read().splitlines()]
    for i in data:
        print(i[1])

    




    
    

    
        
