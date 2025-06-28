# Problema B
# Dança das Leetras

# Exemplos de entrada  Exemplos de Saída
# ABABBA      # 4

# AAAAAA      # 1

# BABABABABA  # 10

palavra=input()
soma=1
maximo=[1]
for i in range(len(palavra)-1):
    if palavra[i]!=palavra[i+1]:
        soma+=1
        maximo.append(soma)
    else: 
        soma=0
print(max(maximo))