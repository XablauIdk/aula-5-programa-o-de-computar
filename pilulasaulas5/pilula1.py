def validarSenha (s):
    if len(s) < 8:
        return 'Senha inválida, muito curta.'
    
    temNumero = False
    temMaiuscula = False
    simbolos ='!@#$%&'
    temSimbolos = False
    for c in senha:
        if c == ' ':
            return 'Senha inválida, não pode ter espaço'
        if c >= '0' and c <='9':
            temNumero = True
        if c >= 'A' and c <= 'Z':
            temMaiuscula = True
        if c in simbolos:
            temSimbolos = True
            
        
    if not temNumero:
        return 'Senha inválida, precisa de um num, pelo menos'
        
    if not temMaiuscula:
        return 'Senha inválida, precisa de uma letra maiuscula'
    
    if not temSimbolos:
        return 'Senha inválida, precisa de um símbolo'
        
    return 'Senha válida'
        
#main  
senha = input('Digite a senha: ')
r = validarSenha(senha)
print(r)