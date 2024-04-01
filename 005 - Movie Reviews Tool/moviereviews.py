import rottentomatoes as rot

filme = input("Digite o nome do filme que você quer ver o sumário (DIGITE O NOME DO FILME CORRETAMENTE E EM INGLES) \n")

print(f"Para o filme {filme}, a nota da critica foi {rot.tomatometer(filme)} e a nota do público foi {rot.audience_score(filme)}")

while True:
    try:
        respostainfos = input("Deseja saber mais informações sobre o filme? (data de lançamento, generos e atores) \n (s/n) \n")
        if respostainfos.lower() == "s":
            print(f"A Data de lançamento do filme {filme} é {rot.year_released(filme)} \n Os filme se enquadra nos generos de {rot.genres(filme)} \n Os Principais atores/atrizes do filme são {rot.actors(filme)}")
            break
        elif respostainfos.lower() == "n":
            print("Obrigado por usar a ferramenta!")
            break
    except ValueError as e:
        print(f"Erro: {e}. Escreva apenas S ou N de resposta.")
        continue