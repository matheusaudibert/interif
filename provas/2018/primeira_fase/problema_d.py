# Problema D 
# Fábrica de Automóveis

# Exemplos de Entradas  Exemplos de Saídas 
# 3 2      5100 6700
# 4 5 7    1700 2200
# 1 2 2
# 300 400  
# 500 600
# 200 300

# 4 3          21200 25800 30400
# 10 11 12 13  28400 34600 40800
# 14 15 16 17
# 300 400 500
# 400 500 600
# 500 600 700
# 600 700 800

# Lê o número de modelos e meses
modelos, meses = map(int, input().split())
# Lê a quantidade de parafusos por modelo
parafusos_por_modelo = list(map(int, input().split()))
# Lê a quantidade de travas por modelo
travas_por_modelo = list(map(int, input().split()))
# Lê a produção de cada modelo em cada mês
producao = []
for _ in range(modelos):
    linha_producao = list(map(int, input().split()))
    producao.append(linha_producao)
# Inicializa os totais por mês com 0
total_parafusos = [0] * meses
total_travas = [0] * meses
# Calcula os totais por mês
for modelo in range(modelos):
    for mes in range(meses):
        quantidade = producao[modelo][mes]
        total_parafusos[mes] += parafusos_por_modelo[modelo] * quantidade
        total_travas[mes] += travas_por_modelo[modelo] * quantidade
# Exibe os resultados separados por tabulação
print('\t'.join(map(str, total_parafusos)))
print('\t'.join(map(str, total_travas)))
