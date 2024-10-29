# Criar uma função que vai pegar o nome e sobrenome de uma pessoa
# O que a função vai fazer: Cadastrar essa pessoa em um aplicativo
# retornar o cadastro da pessoa com um numero de registro .


def cadastrar_pessoa():
    registro = 0
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    
    registro += 1
    
    cadastro = {
        "nome": nome,
        "sobrenome": sobrenome,
        "registro": registro
    }
    
    return f"Cadastro realizado com sucesso!\nNome: {cadastro['nome']}\nSobrenome: {cadastro['sobrenome']}\nRegistro: {cadastro['registro']}"

# Exemplo de uso
pessoa = cadastrar_pessoa()
print("Cadastro realizado com sucesso!")
print(pessoa) 

