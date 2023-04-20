def area_do_retangulo(b, h):
    areacomprimento = b*h
    areaperimetro = 2*(b+h)
    return areacomprimento, areaperimetro

b = float(input("informe a area da base: "))
h = float(input("informe a altura: "))
areafim = b*h
perimetrofim = 2*(b+h)
print ("o retangulo de base: "+str(b)+", e altura: "+str(h)+" tem area total de: "+str(areafim)+", e perimetro de: "+str(perimetrofim))