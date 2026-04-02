def verificarValores():
    anterior = float(input('Leitura 1 : '))
    crescente = True
    
    for i in range(4):
        atual = float(input(f'Leitura {i+2}: '))
        if atual <= anterior:
            crescente = False
            break # return = False
    return crescente # return = True

#main
if verificarValores():
    print('crescente')
else:
    print('instável')