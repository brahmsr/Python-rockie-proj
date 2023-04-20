def area_do_retangulo(b, h):
    areacomprimento = b*h
    return areacomprimento
def perimetro_retangulo(b, h):
    areaperimetro = b+h
    return areaperimetro
b = float(input("informe a area da base: "))
h = float(input("informe a altura: "))
areafim = area_do_retangulo(b, h)
perimetrofim = perimetro_retangulo(b, h)
print ("o retangulo de base: "+str(b)+", e altura: "+str(h)+" tem area total de: "+str(areafim)+", e perimetro de: "+str(perimetrofim))
