def somas(a, b):
    x = a + b
    return x
def multp(a,b):
    y = a * b
    return y

a = float(input("informe o primeiro numero: "))
b = float(input("informe o segundo numero: "))
soma = somas(a, b)
mul = multp(a, b)
print ("o resultado da soma é: "+str(soma))
print("o resultado da multiplicação é: "+str(mul))