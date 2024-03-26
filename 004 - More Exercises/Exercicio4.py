# Exercício 4 - Percentuais
# O Programa deve ler a quantidade total de alunos de uma escola
# O Programa deve ler a quantidade de alunos do sexo masculino
# O Programa deve imprimir o percentual de alunos do sexo masculino e feminino

alunototal = int(input("Coloque o total de alunos:"))
alunomasc = int(input("Coloque o total de alunos do sexo masculino:"))

alunofem = (alunototal - alunomasc)
porcmasc = (alunomasc/alunototal)*100
porcfem = (alunofem/alunototal)*100

print(f"O Número total de alunos na escola é de {alunototal} \n a porcentagem de alunos do sexo masculino no colégio é de {porcmasc:.2f}% \n a porcentagem de alunos do sexo feminino é de {porcfem:.2f}%")