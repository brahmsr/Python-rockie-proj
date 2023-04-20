def media(x, y):
    a = 2/((1/x)+(1/y))
    return a
x = float(input("informe o valor de x: "))
y = float(input("informe o valor de y: "))
mediafim = media(x, y)
print("O resultado da média armonica de: "+str(x)+", e da: "+str(y)+", é a média harmonica: "+str(mediafim))
