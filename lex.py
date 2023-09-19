def analizador_lexico(cadena):
    tokens = []
    estado = 12  # Estado inicial
    buffer = ''  # Almacena el valor del número o espacio
    
    for c in cadena:
        if estado in (12, 13, 14, 15, 16, 17, 18):
            nuevo_estado = reconocer_numero(estado, c)
            if nuevo_estado != -1:
                estado = nuevo_estado
                buffer += c
            else:
                if buffer:
                    print(buffer)
                    tokens.append(("num", buffer))
                    buffer = ''
                estado = 12  # Reiniciar al estado inicial
        elif estado in (22, 23):
            nuevo_estado = reconocer_space(estado, c)
            if nuevo_estado != -1:
                estado = nuevo_estado
                buffer += c
            else:
                if buffer:
                    tokens.append(("space", buffer))
                    buffer = ''
                estado = 12  # Reiniciar al estado inicial
        else:
            # Estado de error, cualquier otro carácter no válido
            buffer += c
            estado = -1
        
    
    # Al final del bucle, si todavía hay contenido en el buffer, se agrega como un token
    if buffer:
        if estado in (12, 13, 14, 15, 16, 17, 18):
            tokens.append(("num", buffer))
        elif estado in (22, 23):
            tokens.append(("space", buffer))
        elif estado == -1:
            tokens.append(("error", buffer))  # Agregar token de error
    
    return tokens

def reconocer_numero(s,c):
    if s==12:
        if c.isdigit():
            return 13
        else:
            return -1
    elif s==13:
        if c.isdigit():
            return 13
        elif c=='.':
            return 14
        elif c=='e' or c=='E':
            return 16
        else:
            return -1
    elif s==14:
        if c.isdigit():
            return 15
        else:
            return -1
    elif s==15:
        if c.isdigit():
            return 15
        elif c=='e' or c=='E':
            return 16
        else:
            return -1
    elif s==16:
        if c=='+' or c=='-':
            return 17
        elif c.isdigit():
            return 18
        else:
            return -1
    elif s==17:
        if c.isdigit():
            return 18
        else:
            return -1
    elif s==18:
        if c.isdigit():
            return 18
        else:
            return -1

def reconocer_space(s,c):
    if s==22:
        if c==' ':
            return 23
        else:
            return -1
    elif s==23:
        if c== ' ':
            return 23
        else:
            return -1

cadena = "34.56E-67  12.34  56E-76  ABC$%^"
tokens = analizador_lexico(cadena)
print(tokens)
for token, valor in tokens:
    print(f"Token: {token}, Valor: {valor}")
