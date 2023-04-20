def transformar_peso(kilos):
    resultado = kilos * 1000
    return resultado

kilos_peso = float(input("informe seu peso em kg: "))
peso_gramas = transformar_peso(kilos_peso)
print("seu peso em gramas:" + str(peso_gramas))