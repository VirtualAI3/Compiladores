def verificarNum(cadena):
    estado = 12
    for c in cadena:
        if estado == 12:
            if c.isdigit():
                estado = 13
            else:
                estado = -1  
                break
        elif estado == 13:
            if c.isdigit():
                estado = 13
            elif c == '.':
                estado = 14
            elif c in ('E','e'):
                estado = 16
            else:
                estado = 20  
                break
        elif estado == 14:
            if c.isdigit():
                estado = 15
            else:
                estado = -1  
                break
        elif estado == 15:
            if c.isdigit():
                estado = 15
            elif c == 'E' or c == 'e':
                estado = 16
            else:
                estado = -1 
                break
        elif estado==16:
            if c=='+' or c=='-':
                estado=17
            elif c.isdigit():
                estado=18
            else:
                estado=-1
                break
        elif estado==17:
            if c.isdigit():
                estado=18
            else:
                estado=-1
                break
        elif estado==18:
            if c.isdigit():
                estado=18
            else:
                estado=-1
                break
    if estado in (13,15,18,20):
        print('Número aceptado')
    else:
        print(f'Carácter {c} no reconocido. Número rechazado')
def verificarNumOtro(cadena):
    estado = 9
    for c in cadena:
        print(f'{estado} + {c}')
        if estado==9:
            if c.isalpha() or c=='_':
                estado=10
            elif c in ('+','-','*,''/'):
                estado=-1
            else: 
                estado=12
        elif estado==10:
            if c.isalpha() or c.isdigit() or c=='_':
                estado=10
            else:
                estado=-1
        elif estado == 12:
            if c.isdigit():
                estado = 13
            else:
                estado = -1  
                break
        elif estado == 13:
            if c.isdigit():
                estado = 13
            elif c == '.':
                estado = 14
            elif c in ('E','e'):
                estado = 16
            else:
                estado = 20
        elif estado == 14:
            if c.isdigit():
                estado = 15
            else:
                estado = -1  
                break
        elif estado == 15:
            if c.isdigit():
                estado = 15
            elif c == 'E' or c == 'e':
                estado = 16
            else:
                estado=21
                break
        elif estado==16:
            if c=='+' or c=='-':
                estado=17
            elif c.isdigit():
                estado=18
            else:
                estado=-1
                break
        elif estado==17:
            if c.isdigit():
                estado=18
            else:
                estado=-1
                break
        elif estado==18:
            if c.isdigit():
                estado=18
            else:
                estado=19
                break
    if estado in (13,15,18,19,20,21):
        print(f'Número {cadena} aceptado')
    elif estado in (10,11):
        print (f'Id {cadena} aceptado')
    else:
        print(f'Carácter {c} no reconocido. {cadena} rechazado')
def verificarIDOtro(cadena):
    estado=9
    resultado=''
    for c in cadena:
        if estado==9:
            if c.isalpha():
                estado=10
                resultado+=c
            else:
                estado=-1
        elif estado==10:
            if c.isalpha() or c.isdigit():
                estado=10
                resultado+=c
            else:
                estado=11
    if estado in (10,11):
        print(f'(ID,{resultado})')
    else:
        print(f'Error en el ID {resultado}')
def verificarID(cadena):
    estado=9
    for c in cadena:
        if estado==9:
            if c.isalpha() or c=='_':
                estado=10
            else:
                estado=-1
                break
        elif estado==10:
            if c.isalpha() or c.isdigit() or c=='_':
                estado=10
            else:
                estado=11
    if estado==10:
        print(f'(ID,{cadena})')
    else:
        print(f'Error en el ID {c}')
def verificarSpace(cadena):
    estado=22
    for c in cadena:
        if estado==22:
            if c==' ':
                estado=23
            else:
                estado=-1
        elif estado==23:
            if c==' ':
                estado=23
            else:
                estado=-1
    if estado==23:
        print(f'Espacio en blanco')
#verificarNumOtro("numero1")
#verificarNumOtro("_suma2")
#verificarNumOtro("n1_2")
#verificarNumOtro("x3y4z_")
#verificarNumOtro("5numero")
#verificarNumOtro("m*2")
#verificarNumOtro("_hola-hola")
#verificarNumOtro("1234e+5")
#verificarNumOtro("23e-24")
#verificarNumOtro("0.3456")
#verificarNumOtro("10.11e12")
#verificarNumOtro("+123")
#verificarNumOtro("123ee")
#verificarNumOtro("123.45e++")
verificarNumOtro("0.3456")