def taxacambio(reais):
    dol= 5.70 * reais
    return dol
reais = float(input("informe o valor em dolares:"))
dols = taxacambio(reais)
print("o seu dinheiro em reais é: " +str(dols))