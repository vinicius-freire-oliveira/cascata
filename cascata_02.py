# Sequência Crescente em Linhas
def sequencia(n):
    # Loop para iterar sobre os números de 1 até n
    for x in range(1, n + 1):
        print(x, end = "\n")  # Imprime o número atual seguido de uma quebra de linha
        # Verifica se é o último número, se sim, encerra o loop
        if x == n:
            break
        else:
            # Loop para imprimir os números menores ou iguais ao número atual na mesma linha
            for y in range(1, n + 1):
                if x >= y:
                    print(y, end = " ")  # Imprime o número atual se ele for menor ou igual ao número da linha atual


n = int(input("Digite um número: "))

sequencia(n)