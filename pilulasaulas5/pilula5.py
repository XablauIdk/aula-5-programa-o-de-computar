def contarNotas(valor):
    for nota in (100,50,20,10,5,2):
        qtd = valor // nota
        valor = valor % nota
        if qtd > 0 :
            print (f'{qtd} notas(s) de R$ {nota}')
           
#main
valor = float(input('Qual o valor: '))
contarNotas(valor)