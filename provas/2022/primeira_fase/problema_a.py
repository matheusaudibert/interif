# import sys
# import numpy as np

# # Entrada
# a, b, c, d, e = map(float, input().split())
# vi, vf = map(int, input().split())
# if vi > vf:
#     vi, vf = vf, vi

# # Derivada de T(x): T'(x) = 4ax^3 + 3bx^2 + 2cx + d
# coeff = [4*a, 3*b, 2*c, d]
# raizes = np.roots(coeff)
# extremos = []

# # Filtra raízes reais dentro do intervalo
# for r in raizes:
#     if np.isreal(r):
#         x = float(np.real(r))
#         if vi <= x <= vf:
#             # Segunda derivada
#             segunda = 12*a*x**2 + 6*b*x + 2*c
#             tipo = 'min' if segunda > 0 else 'max' if segunda < 0 else None
#             if tipo:
#                 extremos.append((x, tipo))

# # Ordena os extremos pela rotação (x)
# extremos.sort()

# # Procura padrão: máximo seguido de mínimo
# for i in range(len(extremos) - 1):
#     if extremos[i][1] == 'max' and extremos[i+1][1] == 'min':
#         print(f"{extremos[i][0]:.7f}")
#         print(f"{extremos[i+1][0]:.7f}")
#         break
# else:
#     print("PARAMETROS FALHOS")
