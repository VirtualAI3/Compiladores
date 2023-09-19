def verificarOprel(cadena):
    estado = 0
    resultado = None

    for c in cadena:
        if estado == 0:
            if c == '<':
                estado = 1
                resultado = "(oprel, LT)"
            elif c == '=':
                estado = 5
                resultado = "(oprel, EQ)"
            elif c == '>':
                estado = 6
                resultado = "(oprel, GT)"
            else:
                resultado = None
                break
        elif estado == 1:
            if c == '=':
                estado = 2
                resultado = "(oprel, LE)"
            elif c == '>':
                estado=3
                resultado = "(oprel, NE)"
            else:
                resultado = None
                break
        elif estado == 6:
            if c == '=':
                estado=7
                resultado = '(oprel, GE)'
            else:
                resultado = None
                break
        elif estado==2:
            if c=='':
                resultado='(oprel, LE)'
            else:
                resultado=None
                break
        elif estado==3:
            if c=='':
                resultado='(oprel,NE)'
            else:
                resultado=None
                break
        elif estado==5:
            if c=='':
                resultado = '(oprel, EQ)'
            else:
                resultado = None
                break
        elif estado==7:
            if c=='':
                resultado='(oprel,GE)'
            else:
                resultado=None
                break
    if resultado is not None:
        print(resultado)
    else:
        print(f'Caracter {c} no reconocido')

verificarOprel(">")
