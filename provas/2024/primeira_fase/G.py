# Problema G
# Notacao Forsyth-Edwards

# Exemplos de Entrada  Exemplos de Saída
# rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR  # |r|n|b|q|k|b|n|r|
                                               # |p|p|p|p|p|p|p|p|
                                               # | | | | | | | | |
                                               # | | | | | | | | |
                                               # | | | | | | | | |
                                               # | | | | | | | | |
                                               # |P|P|P|P|P|P|P|P|
                                               # |R|N|B|Q|K|B|N|R|
                                            
# r1bk3r/p2pBpNp/n4n2/1p1NP2P/6P1/3P4/P1P1K3/q5b1  # |r| |b|k| | | |r|
                                                   # |p| | |p|B|p|N|p|
                                                   # |n| | | | |n| | |
                                                   # | |p| |N|P| | |P|
                                                   # | | | | | | |P| |
                                                   # | | | |P| | | | |
                                                   # |P| |P| |K| | | |
                                                   # |q| | | | | |b| |

string_fen=input()
fileiras_fen=string_fen.split('/')
for fileira_fen in fileiras_fen:
    fileira_tabuleiro=[]
    for caractere in fileira_fen:
        if caractere.isdigit():
            fileira_tabuleiro.extend([' ']*int(caractere))
        else:
            fileira_tabuleiro.append(caractere)
        print('|'+'|'.join(fileira_tabuleiro)+'|')

