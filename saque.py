def dinheiro():
    din = float(input("Quanto tem em sua conta bancária: "))
    gg= float(input("deseja sacar ou depositar? responda com SAQUE=1 ou DEPOSITO=2: "))
    if gg==1:
        a= float(input("informe a quantidade do saque: "))
        b= din - a
        print("o valor de sua conta agora é: "+str(b))
    elif gg==2:
        c= float(input("informe a quantidade do depósito: "))
        d = c + din
        print ("o valor da sua conta agora é: "+str(d))

x= dinheiro()