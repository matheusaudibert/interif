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
