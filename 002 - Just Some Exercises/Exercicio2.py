# Exercicio 2
print("Troca de Números")
n1 = int(input("Escolha o Primeiro Número:"))
n2 = int(input("Escolha o Segundo Número:"))

print(f"Os Números selecionados foram {n1} e {n2}!")
print("Aguarde, a troca está sendo feita!")

n1, n2 = n2, n1

print(f"Os Números trocados foram {n1} e {n2}!")