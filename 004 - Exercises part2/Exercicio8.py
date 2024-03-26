area = float(input("informe o tamanho da area a ser pintada em m²: "))
tintaLitros = area / 3

latas = tintaLitros / 18

precoLatas = latas * 80

print(f"Serão necessárias {latas} latas, custando R$ {precoLatas} no total")