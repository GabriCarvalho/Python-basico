idade = input("Digite sua idade: ")

if int(idade) >= 5 and int(idade) <= 7:
    print("Infantil A")
elif int(idade) >= 8 and int(idade) <= 10:
    print("Infantil B")
elif int(idade) >= 11 and int(idade) <= 13:
    print("Juvenil A")
elif int(idade) >= 14 and int(idade) <= 17:
    print("Juvenil B")
else:
    print("Nao tem idade para competir nesse Campeonato")


