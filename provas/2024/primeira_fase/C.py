# Problema C
# Fila

# Exemplos de Entrada  Exemplos de Saída

# CHEGADA ALEXSSANDRA 21  # ALEXSSANDRA
# CHEGADA AIRTON 19       # AIRTON
# CHEGADA ROBERTO 23      # MARIANA
# CHEGADA MARIO 54        # SERGIO
# ATENDIMENTO             # ADEMIR
# CHEGADA EVELINE 16      # ROBERTO
# ATENDIMENTO             # MARIO
# CHEGADA MARIANA 59      # EVELINE
# CHEGADA SERGIO 55       # CAMILA
# ATENDIMENTO             # ANDRE
# CHEGADA CAMILA 20
# ATENDIMENTO
# CHEGADA ADEMIR 65
# ATENDIMENTO
# CHEGADA ANDRE 17
# ATENDIMENTO
# ATENDIMENTO
# ATENDIMENTO
# ATENDIMENTO
# ATENDIMENTO

# CHEGADA ERICK 17        # GUSTAVO
# CHEGADA GUSTAVO 66      # ERICK
# ATENDIMENTO             # HAMILTON
# CHEGADA BRUNA 19        # BRUNA
# ATENDIMENTO
# CHEGADA HAMILTON 57
# ATENDIMENTO
# ATENDIMENTO

fila_prioridade = []
fila_normal = []
saidas=[]
while True:
    linha=input().strip()
    if linha.startswith("CHEGADA"):
      _,nome,idade=linha.split()
      idade=int(idade)
      if idade>54:
        fila_prioridade.append(nome)
      else:
        fila_normal.append(nome)
    elif linha=="ATENDIMENTO":
      if fila_prioridade:
        saidas.append(fila_prioridade.pop(0))
      elif fila_normal:
        saidas.append(fila_normal.pop(0))
      if not fila_prioridade and not fila_normal:
        break
for nome in saidas:
    print(nome)