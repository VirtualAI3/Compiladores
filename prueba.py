def operel(s, c):
    if s == 0:
        if c == '<':
            sg = 1
        elif c == '>':
            sg = 6
        elif c == '=':
            sg = 5
        else:
            sg = 0
    elif s == 1:
        if c == '<':
            sg = 0
        elif c == '>':
            sg = 3
        elif c == '=':
            sg = 2
        elif c=='':
            sg=4
        else:
            sg = 4
    elif s == 6:
        if c == '<':
            sg = 0
        elif c == '>':
            sg = 0
        elif c == '=':
            sg = 7
        else:
            sg = 8
    return sg

cad = '>='
estado = 0

for c in cad:
    estado = operel(estado, c)

if estado in (1,2,3,5,7,6):
    print(cad, "es aceptado :)")
else:
    print(cad, "no es aceptadp :(")