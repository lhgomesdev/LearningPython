  # Exercicio 1
print("Compra de moeda estrangeira \n Dolar = RS5 \n Euro = R$6 \n Yuan Chinês = R$0,69 \n Iene Japonês = R$0,034")
dolar = 5
euro = 6
yuan = 0.69
iene = 0.034

while True:
      escolha_moeda = input("Qual moeda deseja comprar?")
      if escolha_moeda == "dolar":
          preco_compra = dolar
          break
      elif escolha_moeda == "euro":
          preco_compra = euro
          break
      elif escolha_moeda == "yuan":
          preco_compra = yuan
          break
      elif escolha_moeda == "iene":
          preco_compra = iene
          break
      else:
          print("Opção de moeda inválida. Tente novamente.")
quantidade = int(input("Quantas moedas você deseja comprar?"))
preco_total = quantidade * preco_compra
print(f"Você está comprando {quantidade} de {escolha_moeda} por R$ {preco_total:.2f}.")
resposta_compra = input(f"Você deseja comprar {escolha_moeda} por {preco_total:.2f}? (sim/não)")
if resposta_compra.lower() != "não" and resposta_compra.lower() != "n":
    print(f"Você comprou {escolha_moeda} por {preco_total:.2f}!")