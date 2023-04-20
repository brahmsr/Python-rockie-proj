def calcular_passe(a):
 resultado = False
name=input("informe o seu nome: ")
nota = float(input("informe a sua nota: "))
if nota>=60:
     resultado=True
     msg1="Parabéns "+str(name)+", você passou, sua nota: "+str(nota)+" foi maior que 60"
     print(msg1)
else:
    resultado=False
    msg2=str(name)+" mais sorte na proxima vez, sua nota: "+str(nota)+" foi menor que 60"
    print (msg2)