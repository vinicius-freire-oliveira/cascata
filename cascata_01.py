# Cascata de números baseado no número digitado
# Cada linha corresponderá a repetição do número correspondente a sua linha, ou seja, 1 será
# impresso uma vez na primeira linha, 2 impresso duas vezes na linha dois e assim por diante
def cascata(n):
    # Loop para iterar sobre as linhas da cascata
    for x in range(1, n + 1):
        print(end = "\n")  # Imprime uma nova linha para cada linha da cascata
        # Loop para iterar sobre os elementos de cada linha da cascata
        for y in range(1, n + 1):
            # Verifica se o elemento atual deve ser impresso com base na posição na cascata
            if x >= y:
                print(x, end = " ")  # Imprime o número da linha atual

n = int(input("Digite um número: "))

cascata(n)