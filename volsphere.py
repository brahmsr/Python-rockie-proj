def volume_esfera(raio):
    pi = 3.14
    volume = (4/3) * pi * (raio**3)
    return volume

raio = float(input("qual o raio da esfera: "))
vol = volume_esfera(raio)
print ("o volume da seguinte esfera de raio" +str(raio) +" é " +str(vol))