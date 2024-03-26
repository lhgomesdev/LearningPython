# Exercício 5 - Impostos
#O programa deve ler o valor total da manutenção de um veículo (valor_total)
#O programa deve ler o percentual de impostos de serviços (imp_serv)
#O programa deve ler o percentual de impostos de produtos (imp_prod)
#O programa deve imprimir o total a ser pago nos dois impostos, bem como o valor que sobra depois de descontado os impostos. 

valortotal = float(input("Informe o valor total da manutenção do seu veículo: "))

impServ = float(input("Informe o percentual de impostos de serviços: "))
impProd = 100 - impServ

servTotal = valortotal * (impServ/100)
prodTotal = valortotal * (impProd/100)
impTotal = prodTotal + servTotal
restante = valortotal - impTotal

print(f"O valor total a ser pago nos impostos de serviços é de R$ {servTotal:.2f}")
print(f"O valor total a ser pago nos impostos de produtos é de R$ {prodTotal:.2f}")
print(f"O valor total a ser pago nos impostos é de R$ {impTotal:.2f}")

print(f"O valor que sobra depois de descontar os impostos é de R$ {restante:.2f}")