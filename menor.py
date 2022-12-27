def menorString():
    resp = 'S'
    lista = []
    while resp in 'Ss':
        num = lista.append(str(input('digite uma palavra '))) 
        resp = str(input('quer continuar [S/N] ')).upper().strip()[0]
    menor = min(lista)
    return menor
x = menorString()
print(x)
    

    



        
    
    
        
       
    
