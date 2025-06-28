# Problema B 
# Jogo de Truco

# Exemplos de Entradas  Exemplos de Saídas 
# 1   2 3 

# 11  12 13 1 2 3 

# 13  1 2 3 

# 3   0 

cartas = [4, 5, 6, 7, 11, 12, 13, 1, 2, 3]
carta = int(input())

maiores = [c for c in cartas if cartas.index(c) > cartas.index(carta)]
if maiores:
    print(*maiores)
else:
    print(0)