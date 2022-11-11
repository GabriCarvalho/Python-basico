idade = input("Digite sua idade: ")
if int(idade) <= 16:
    print("Voce eh menor de idade")
elif int(idade) > 16 and int(idade) <= 18:
    print("Emancipado")
else:
    print("Voce eh maior de idade")

