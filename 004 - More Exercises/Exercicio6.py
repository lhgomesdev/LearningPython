# Exercicio 6 - Calculadora de horas trabalhadas

while True:

    horasValor = float(input("Informe o quanto você ganha por hora: "))
    horasTrab = float(input("Informe as suas horas trabalhadas no mês: "))
    if horasTrab >= 730:
        print("O Número de horas trabalhadas não pode ser maior que o mês")
    else:        
        horasTotal = horasValor * horasTrab
        print(f"O salário do mês foi: R$ {horasTotal}")
        break