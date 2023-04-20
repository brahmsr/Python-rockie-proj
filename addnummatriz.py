def matrizpar(q):
    linhas = len(q)
    colunas = len (q[0])
    for i in range (0, linhas):
        for j in range(0, colunas):
            if (i+j)%2==0:
                q [i] [j] = ["par"]
            else:
                q [i] [j] = ["ímpar"]
    return q

N = int(input("Informe um número inteiro N: "))
M = int(input("Informe um número inteiro M: "))

matriz = []
for i in range(0, N):
    linha = []
    for j in range (0, M):
        linha.append(1)
    matriz.append(linha)

matriz = matrizpar(matriz)
for i in range(0, N):
    print(matriz [i])
