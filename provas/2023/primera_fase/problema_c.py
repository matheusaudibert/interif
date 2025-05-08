# Problema C 
# O Tesouro dos Números Primos

def crivo_eratostenes(limite):
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False  
    
   
    for i in range(2, int(limite ** 0.5) + 1):
        if primos[i]: 
            for j in range(i * i, limite + 1, i):
                primos[j] = False 
    return [num for num, is_primo in enumerate(primos) if is_primo]

N = int(input("Digite o valor de N: "))

primos = crivo_eratostenes(N)

print(" ".join(map(str, primos)))

