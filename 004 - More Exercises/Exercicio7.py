# Exercício 7 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal
# utilizando as seguintes fórmulas:  homens: P = 72,7h - 58  mulheres: P = 62,1h - 44,7 e mostre o valor do peso ideal para homens e mulheres.

altura = float(input("Qual sua altura?"))
peso = float(input("Qual seu peso?"))

while True:
    genero = input("Qual seu Genero? (Homem/Mulher)")
    if genero.lower() == "homem":
        peso_ideal = (72.7 * altura) - 58
        print(f"Seu peso ideal é de {peso_ideal:.2f}kg")
        break
    elif genero.lower() == "mulher":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é de {peso_ideal:.2f}kg")
        break


