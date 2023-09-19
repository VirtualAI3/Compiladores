import itertools
def afd(s,c):
    if s==0:
        if c=='a':
            return 1
        elif c=='b':
            return 0
    elif s==1:
        if c=='a':
            return 1
        elif c=='b':
            return 2
    elif s==2:
        if c=='a':
            return 1
        elif c=='b':
            return 3
    elif s==3:
        if c=='a':
            return 1
        elif c=='b':
            return 0
def verificar(cadena):
    estado=0
    for c in cadena:
        estado=afd(estado,c)
    if estado==3:
        print(f'La cadena {cadena} es aceptada')
    else:
        print(f'La cadena {cadena} es rechazada')
def oprel(s,c):
    if s==0:
        if c=='<':
            return 1
        elif c=='=':
            #return 5
            return '(oprel, EQ)'
        elif c=='>':
            return 6
    elif s==1:
        if c=='=':
            #return 2
            return '(oprel, LE)'
        elif c=='>':
            #return 3
            return '(oprel, NE)'
        else:
            #return 4
            return '(oprel, LT)'
    elif s==2:
        return '(oprel, LE)'
    elif s==3:
        return '(oprel, NE)'
    elif s==4:
        return '(oprel, LT)'
    elif s==5:
        return '(oprel, EQ)'
    elif s==6:
        if c=='=':
            #return 7
            return '(oprel,GE)'
        else:
            #return 8
            return '(oprel,GT)'
    elif s==7:
        return '(oprel,GE)'
    elif s==8:
        return '(oprel,GT)'
    else:
        return 'Caracter no reconocido'
def verificarOprel(cadena):
    estado=0
    if len(cadena)==1:
        cadena=itertools.chain(cadena,'o')
    for c in cadena:
        estado=oprel(estado,c)
    print(estado)
verificarOprel("=")