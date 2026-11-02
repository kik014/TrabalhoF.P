idade = int(input("Digite a sua idade: "))
if idade < 13:
    print("Você é uma criança.")
elif idade < 18:
    print("Você é um adolescente.")
elif idade < 50:
    print("Você é um adulto.")
elif idade < 65:
    print("Você é um adulto mais velho.")
elif idade < 80:
    print("Você é um idoso.")
elif idade < 100:
    print("Você é um dinossauro.")
else:
    print("Você é um fóssil.")

#notas do exame
nota_exame = float(input("Digite a sua nota de exame: "))
if nota_exame >= 9.5:
    print("Aprovou na UC")
else:
    print("Fazer recurso ")

#nota de recurso
nota_recurso = float(input(" Submeta a sua nota de recurso: "))
if nota_recurso >= 9.5:
    print("Passou na UC")
else:
    print("Reprovou na UC")

# contador de números pares e ímpares
contador = 1
while contador <= 10:
    print(contador)
    contador = contador + 1

print("Fim")

contador = 10
while contador >= 1:
    print(contador)
    contador = contador - 1
print("Fim")

#pares
contador = 1
while contador <= 10:
    if contador % 2 == 0:
        print(contador)
    contador = contador + 1

print("Fim")
contador = 1
while contador <= 10:
    if contador % 2 == 0 and contador != 4:
        print(contador)
    contador = contador + 1

print("Fim")

contador = 1
while contador <= 10:
    if contador > 6:
        break
    if contador % 2 == 0:
        print(contador)
    contador = contador + 1

print("Fim")

#outra cn
contador = 1
while contador <= 10:
    if contador > 6:
        break
    if contador % 2 == 0:
        print(contador)
    contador = contador + 1
else:
    print("Concluiu todas as iterações")

print("Fim")
