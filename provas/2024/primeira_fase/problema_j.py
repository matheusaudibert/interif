competidores = int(input())
saltos_por_competidor = int(input())

maior_salto = -1.0
vencedor = ""

for _ in range(competidores):
    nome = input().strip()
    for _ in range(saltos_por_competidor):
        entrada = input().strip()
        if entrada.upper().endswith(' I'):
            salto = 0.0
        else:
            salto = float(entrada)
        if salto > maior_salto:
            maior_salto = salto
            vencedor = nome

# Exibir resultado
print(vencedor)  # nome
print(maior_salto)  # salto
