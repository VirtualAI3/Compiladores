def verificarNumOID(cadena):
    estado = 9
    resultado=''
    for c in cadena:
        if estado == 9:
            if c.isalpha() or c == '_':
                estado = 10
            elif c in ('+', '-', '*', '/'):
                estado = -1
            elif c.isdigit():
                estado = 13
                resultado+=c
            else:
                estado = 12
        elif estado == 10:
            if c.isalpha() or c.isdigit() or c == '_':
                estado = 10
            else:
                estado = -1
        elif estado == 12:
            if c.isdigit():
                estado = 13
                resultado+=c
            else:
                estado = -1
                break
        elif estado == 13:
            if c.isdigit():
                estado = 13
                resultado+=c
            elif c == '.':
                estado = 14
                resultado+=c
            elif c in ('E', 'e'):
                estado = 16
                resultado+=c
            else:
                estado = 20
        elif estado == 14:
            if c.isdigit():
                estado = 15
                resultado+=c
            else:
                estado = -1
                break
        elif estado == 15:
            if c.isdigit():
                estado = 15
                resultado+=c
            elif c in ('E', 'e'):
                estado = 16
                resultado+=c
            else:
                estado = 21
                break
        elif estado == 16:
            if c in ('+', '-'):
                estado = 17
                resultado+=c
            elif c.isdigit():
                estado = 18
                resultado+=c
            else:
                estado = -1
                break
        elif estado == 17:
            if c.isdigit():
                estado = 18
                resultado+=c
            else:
                estado = -1
                break
        elif estado == 18:
            if c.isdigit():
                estado = 18
                resultado+=c
            else:
                estado = 19
                break
    if estado in (13, 15, 18, 19, 20, 21):
        print(f'Número {resultado} aceptado')
    elif estado in (10, 11):
        print(f'Id {cadena} aceptado')
    else:
        print(f'Carácter {c} no reconocido. {cadena} rechazado')

verificarNumOID("0.34e-3%")
