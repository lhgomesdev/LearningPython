# Exercício 8 - Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# A tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
# Para simplificação nesse momento, não se preocupe em arredondar a quantidade de latas a serem compradas

area = float(input("informe o tamanho da area a ser pintada em m²: "))
tintaLitros = area / 3

latas = tintaLitros / 18

precoLatas = latas * 80

print(f"Serão necessárias {latas} latas, custando R$ {precoLatas} no total")