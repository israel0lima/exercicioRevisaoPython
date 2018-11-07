print("Temos: Filé duplo, Alcatra e Picanha")

Escolha = input("Escolha apenas um tipo de carne com quantidade indeterminada: ")

#condição

if Escolha == "Filé duplo":
    print("Até 5kg são R$ 4,90 por Kg do Filé, passando disso fica 5.80")
    Kg = int(input("Quantos Kilos vc deseja levar?: "))
    if Kg > 5:
        preco = 5.80
        valor = preco * Kg
        cartao = input("Você tem o cartão tabajara?: ")
        if cartao == "sim":
            porcent = (((5/100)*valor)- valor)
            valorT = valor - porcent
            print("Você terá que pagar %s R$ no cartão tabajara"%(valorT))
            print("Levará %s Kg de Filé duplo"%(Kg))
        else:
            print("Você terá que pagar %s R$ à vista"%(valor))
            print("Levará %s Kg de Filé duplo"%(Kg))
    else:
        preco = 4.90
        valor = preco * Kg
        cartao = input("Você tem o cartão tabajara?: ")
        if cartao == "sim":
            porcent = (((5/100)*valor)- valor)
            valorT = valor - porcent
            print("Você terá que pagar %s R$ no cartão tabajara"%(valorT))
            print("Levará %s Kg de Filé duplo"%(Kg))
        else:
            print("Você terá que pagar %s R$ à vista"%(valor))
            print("Levará %s Kg de Filé duplo"%(Kg))
        

elif Escolha == "Alcatra":
    print("Até 5kg são R$ 5,90 por Kg de Alcatra, passando disso fica 6,80")
    Kg = int(input("Quantos Kilos vc deseja levar?: "))
    if Kg > 5:
        preco = 6.80
        valor = preco * Kg
        cartao = input("Você tem o cartão tabajara?: ")
        if cartao == "sim":
            porcent = (((5/100)*valor)- valor)
            valorT = valor - porcent
            print("Você terá que pagar %s R$ no cartão tabajara"%(valorT))
            print("Levará %s Kg de Alcatra"%(Kg))
        else:
            print("Você terá que pagar %s R$ à vista"%(valor))
            print("Levará %s Kg de Alcatra"%(Kg))
    else:
        preco = 5.90
        valor = preco * Kg
        cartao = input("Você tem o cartão tabajara?: ")
        if cartao == "sim":
            porcent = (((5/100)*valor)- valor)
            valorT = valor - porcent
            print("Você terá que pagar %s R$ no cartão tabajara"%(valorT))
            print("Levará %s Kg de Alcatra"%(Kg))
        else:
            print("Você terá que pagar %s R$ à vista"%(valor))
            print("Levará %s Kg de Alcatra"%(Kg))

elif Escolha == "Picanha":
    print("Até 5kg são R$ 6,90 por Kg de Picanha, passando disso fica 7,80")
    Kg = int(input("Quantos Kilos vc deseja levar?: "))
    if Kg > 5:
        preco = 7.80
        valor = preco * Kg
        cartao = input("Você tem o cartão tabajara?: ")
        if cartao == "sim":
            porcent = (((5/100)*valor)- valor)
            valorT = valor - porcent
            print("Você terá que pagar %s R$ no cartão tabajara"%(valorT))
            print("Levará %s Kg de Picanha"%(Kg))
        else:
            print("Você terá que pagar %s R$ à vista"%(valor))
            print("Levará %s Kg de Picanha"%(Kg))
    else:
        preco = 6.90
        valor = preco * Kg
        cartao = input("Você tem o cartão tabajara?: ")
        if cartao == "sim":
            porcent = (((5/100)*valor)- valor)
            valorT = valor - porcent
            print("Você terá que pagar %s R$ no cartão tabajara"%(valorT))
            print("Levará %s Kg de Picanha"%(Kg))
        else:
            print("Você terá que pagar %s R$ à vista"%(valor))
            print("Levará %s Kg de Picanha"%(Kg))




