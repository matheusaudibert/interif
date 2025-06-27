# Problema B 
# Jogo de Truco

# Exemplos de Entradas  Exemplos de Saídas 
# 1   2 3 
# 11  12 13 1 2 3 
# 13  1 2 3 
# 3   0 

# Define a ordem de força das cartas, da mais fraca para a mais forte.
# A força é determinada pela posição (índice) na lista.
cartas = [4, 5, 6, 7, 11, 12, 13, 1, 2, 3]
# Lê a carta do usuário.
carta = int(input())
# Cria uma lista com as cartas que são mais fortes que a carta do usuário.
# A comparação é feita com base no índice da carta na lista 'cartas': um índice maior significa uma carta mais forte.
maiores = [c for c in cartas if cartas.index(c) > cartas.index(carta)]
# Se a lista 'maiores' não estiver vazia, imprime seus elementos.
if maiores:
    # O '*' desempacota a lista para imprimir os elementos separados por espaço.
    print(*maiores)
# Caso contrário, se não houver cartas maiores, imprime 0.
else:
    print(0)