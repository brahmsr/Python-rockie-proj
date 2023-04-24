operador = input ("entre com um operador (+ - * /): ")
num1 = float(input("entre com o primeiro numero: "))
num2 = float(input("entre com o segundo numero: "))

if operador == "+":
    resultado= num1 + num2
    print(round(resultado ,3))
    
elif operador == "-":
    resultado= num1 - num2
    print(round(resultado ,3))
    
elif operador == "*":
    resultado= num1 * num2
    print(round(resultado ,3))
    
elif operador == "/":
    resultado= num1 / num2
    print(round(resultado ,3))

else:
    print(f"{operador} não é um comando valido")