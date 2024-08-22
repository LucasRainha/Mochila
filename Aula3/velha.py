def temEspaco(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            if matriz[linha][coluna] == ' ':
                return True
    return False

def haGanhador(matriz):


matriz = []

tab = []

for i in range(3):
    tab.append([' '] * 3)

tab[1][0] = 'O'
tab[2][0] = 'O'
tab[1][1] = 'X'
tab[0][2] = 'X'

for linha in tab:
    print(linha)

print(temEspaco(tab))