# Lê a string FEN da entrada
string_fen = input()

# Divide a string em 8 partes, uma para cada fileira do tabuleiro
fileiras_fen = string_fen.split('/')

# Itera sobre cada fileira descrita na notação FEN
for fileira_fen in fileiras_fen:
    fileira_tabuleiro = []
    # Itera sobre cada caractere na descrição da fileira
    for caractere in fileira_fen:
        if caractere.isdigit():
            # Se for um número, adiciona a quantidade correspondente de espaços vazios
            fileira_tabuleiro.extend([' '] * int(caractere))
        else:
            # Se for uma letra, adiciona a peça
            fileira_tabuleiro.append(caractere)
    
    # Imprime a fileira do tabuleiro formatada
    print('|' + '|'.join(fileira_tabuleiro) + '|')

