# Problema J
# Salto em Distância

# Exemplos de Entrada  Exemplos de Saída
# 3        # Beatriz 
# 4
# Beatriz  
# 7.12
# 6.54 I
# 7.34
# 0.0 I
# Isabel
# 3.45 I
# 7.12
# 7.52
# 5.67
# Alice
# 0.0 I
# 7.59
# 0.0
# 7.12 I

# 3        # Isabel
# 4        # 7.52
# Beatriz
# 7.12
# 6.54 I
# 7.34
# 0.0 I
# Isabel
# 3.45 I
# 7.12
# 7.52
# 5.67
# Alice
# 0.0 I
# 7.59 I
# 0.0
# 7.12 I

competidores=int(input())
saltos_por_competidor=int(input())
maior_salto=-1.0
vencedor = ""
for _ in range(competidores):
    nome=input().strip()
    for _ in range(saltos_por_competidor):
        entrada=input().strip()
        if entrada.upper().endswith(' I'):
            salto=0.0
        else:
            salto=float(entrada)
        if salto>maior_salto:
            maior_salto=salto
            vencedor=nome
print(vencedor)
print(maior_salto)
