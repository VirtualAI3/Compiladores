def thenAFD(s,c):
    if s==0:
        if c=='t':
            return 1
        else:
            return -1
        
    elif s==1:
        if c=='h':
            return 2
        else:
            return -1
    elif s==2:
        if c=='e':
            return 3
        else:
            return -1
    elif s==3:
        if c=='n':
            return 4
        else:
            return -1
    elif s==4:
        return 5
    else:
        return -1
def verificarThen(c):
    estado=0
    for c in c:
        if estado!=-1:
            estado=thenAFD(estado,c)
        else:
            break
    if estado!=-1:
        print ('then')
    else:
        print (f'Caracter {c} no reconocido') 
verificarThen('then ')