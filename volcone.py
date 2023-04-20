def volcone(raio):
    pi = 3.14
    vol = pi*(raio**2)/3
    return vol
raio = float(input("informe o valor do raio em cm: "))
volume= volcone(raio)
print("o volume do seu cone em cm é: " +str(volume))