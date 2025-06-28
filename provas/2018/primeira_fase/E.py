# Problema E 
# Imposto de Renda

#Exemplos de Entrada  Exemplos de Saída    
# 1000 3 900   Isento 

# 2999 2 6000  Isento 

# 3000 0 0     1950 

# 3000 1 0     1755 

# 3000 0 263   1687 

# 5000 2 0     520

salario_mensal, n_de_dependentes, gasto_saude = map(int, input().split())
if salario_mensal <= 2999:
  print('Isento')
else:
  salario_anual = salario_mensal * 13
  if salario_mensal <= 4999:
    aliquota = 0.05
  elif salario_mensal <= 9999:
    aliquota = 0.10
  elif salario_mensal <= 14999:
    aliquota = 0.15
  elif salario_mensal <= 19999:
    aliquota = 0.20
  elif salario_mensal <= 24999:
    aliquota = 0.25
  elif salario_mensal <= 29999:
    aliquota = 0.30
  else:
    aliquota = 0.35
  imposto_bruto = salario_anual * aliquota
  percentual_desconto_dependentes = 0
  if n_de_dependentes == 1:
    percentual_desconto_dependentes = 0.10
  elif n_de_dependentes == 2:
    percentual_desconto_dependentes = 0.20
  elif n_de_dependentes >= 3:
    percentual_desconto_dependentes = 0.30
  valor_desconto_dependentes = imposto_bruto * percentual_desconto_dependentes
  limite_desconto_saude = imposto_bruto * 0.15
  valor_desconto_saude = min(gasto_saude, limite_desconto_saude)
  imposto_final = imposto_bruto - valor_desconto_dependentes - valor_desconto_saude
  print(f"{imposto_final:.0f}")

