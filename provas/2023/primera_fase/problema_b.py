# Problema B 
# Classificação para corrida de kart

def converte_tempo(tempo_str):
    # Converte o tempo no formato m:ss.fff para milissegundos.
    minutos, resto = tempo_str.split(":")
    segundos, milissegundos = resto.split(".")
    return int(minutos) * 60000 + int(segundos) * 1000 + int(milissegundos)

def formata_tempo(ms):
    # Converte o tempo em milissegundos de volta para o formato m:ss.fff.
    minutos = ms // 60000
    segundos = (ms % 60000) // 1000
    milissegundos = ms % 1000
    return f"{minutos}:{segundos:02}.{milissegundos:03}"

# Entrada de dados
a, b, c = map(int, input().split())  # número de pilotos, voltas e voltas inválidas
nomes = [input().strip() for _ in range(a)]  # nome dos pilotos

# Criar o dicionário de siglas para nome
siglas_para_nome = {nome[:3].upper(): nome.capitalize() for nome in nomes}

# Dicionário para armazenar o melhor tempo de cada piloto
melhores_tempos = {sigla: float('inf') for sigla in siglas_para_nome}

# Registrar os tempos das voltas
voltas_registradas = []

# Lê as voltas registradas
for _ in range(b):
    sigla, tempo_str = input().split()
    tempo_ms = converte_tempo(tempo_str)
    voltas_registradas.append((sigla, tempo_ms))

# Lê as voltas inválidas
voltas_invalidas = set()
for _ in range(c):
    sigla, tempo_str = input().split()
    tempo_ms = converte_tempo(tempo_str)
    voltas_invalidas.add((sigla, tempo_ms))

# Processar as voltas válidas
for sigla, tempo_ms in voltas_registradas:
    if (sigla, tempo_ms) not in voltas_invalidas:
        if tempo_ms < melhores_tempos[sigla]:
            melhores_tempos[sigla] = tempo_ms

# Criar a lista de resultados
resultado = []
for sigla, tempo_ms in melhores_tempos.items():
    nome = siglas_para_nome[sigla]
    tempo_formatado = formata_tempo(tempo_ms)
    resultado.append((tempo_ms, nome, tempo_formatado))

# Ordenar a lista com base no tempo de volta (menor para maior)
# A ordenação já está levando em conta o tempo e, em caso de empate, a ordem de chegada das voltas
resultado.sort(key=lambda x: x[0])

# Exibir a classificação final
for i, (_, nome, tempo_formatado) in enumerate(resultado, 1):
    print(f"{i} {nome} {tempo_formatado}")
