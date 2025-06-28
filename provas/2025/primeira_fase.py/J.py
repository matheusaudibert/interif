# Problema J
# Cofre Mágico

# Exemplos de entrada  Exemplos de Saída
# 5             # 12
# 10 15 12 8 9

# 3             # 36
# 6 28 36

# 4             # 7
# 7 11 13 17

def numero_de_divisores(n):
    dividores=0
    for i in range(1, n + 1):
        if n % i==0:
            dividores+=1
    return dividores

num=int(input())
if num==0:
  exit()
numeros=list(map(int, input().split()))
n_divisores_primeiro=0
for numero in numeros:
  divisores=numero_de_divisores(numero)
  if divisores>n_divisores_primeiro:
    primeiro=numero
    n_divisores_primeiro=divisores
  if divisores==n_divisores_primeiro:
    if numero<primeiro:
      primeiro = numero
print(primeiro)
    

