vetor1 = []
vetor2 = []
vetor3 = []

vetor1.append(' ')
vetor1.append(' ')
vetor1.append('x')

vetor2.append('o')
vetor2.append('x')
vetor2.append(' ')

vetor3.append('o')
vetor3.append(' ')
vetor3.append(' ')

matriz = []

matriz.append(vetor1)
matriz.append(vetor2)
matriz.append(vetor3)


for vetor in matriz:
    print(vetor)

print('--------------------------------------')

tab = []

for i in range(3):
    tab.append([' '] * 3)

tab[1][0] = 'O'
tab[2][0] = 'O'
tab[1][1] = 'X'
tab[0][2] = 'X'

for linha in tab:
    print(linha)


print('-------------------------------------')

ricardo = []
i = 0
while i < 4:
    ricardo.append([0] * 5)
    i +=1

for pedro in ricardo:
    print(pedro)

print('-------------------------------------')

mat = []
num = 1
for linha in range(4):
    for coluna in range(5):
        mat[linha][coluna] = num
        num = num + 1

for linha in mat:
    print(linha)