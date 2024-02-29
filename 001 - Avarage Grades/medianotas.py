# CODIGO PARA CALCULAR MEDIA DE ALUNOS

def calcular_media(notas):
    # Verifica se a lista de notas não está vazia para evitar divisão por zero
    if len(notas) == 0:
        return 0  
    else:
        # Calcula a média das notas
        media = sum(notas) / len(notas) 
        return media  

# O While é utilizado como função de loop em todo o código abaixo
while True:

    nome_aluno = input("Digite o nome do aluno(a): ")

    try:
        quantidade_notas = int(input("Quantas notas o aluno possui? "))
        if quantidade_notas < 0:
            raise ValueError("Número de notas não pode ser negativo.")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira um número válido de notas.")
        continue

    if quantidade_notas == 0:
        print(f"O aluno(a) {nome_aluno} não possui notas.")
        continue

    # Cria uma lista vazia pra armazenar as notas
    notas_do_aluno = []

    # Loop que irá solicitar as notas ao usuário quantidade_notas vezes
    for i in range(quantidade_notas):

        try:
            nota = float(input(f"Digite a nota {i+1}: "))
            if nota < 0 or nota > 10:
                raise ValueError("A nota deve estar entre 0 e 10.")
        except ValueError as e:
            print(f"Erro: Por favor, insira uma nota válida.")
            break
        else:
            # Adiciona a nota à lista notas_do_aluno
            notas_do_aluno.append(nota)
    else:
        media = calcular_media(notas_do_aluno)
        print(f"A média das notas do aluno(a) {nome_aluno} é: {media:.2f}")

    resposta = input("Deseja calcular a média para outro aluno? (s/n): ")
    if resposta.lower() != "s" and resposta.lower() != "sim":
     break
