numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")

idade = int(input("Digite a sua idade: "))
if 13 <= idade < 18:
    print("Você é um adolescente.")

# preços dos bilhetes
idade = int(input("Digite a sua idade: "))
if idade < 5:
    print("Entrada gratuita.")
elif 5 <= idade < 10:
    print("O preço é 5 euros.")
elif 11 <= idade < 64:
    print("O preço é 20 euros.")
elif 65 <= idade <= 100:
    print("O preço é 5 euros.")
elif idade == 100:
    print("O preço é 0 euros.") 

#Notas e médias
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: ")) 
nota3 = float(input("Digite a terceira nota: "))
if nota1 < 7.5 or nota2 < 7.5 or nota3 < 7.5:
    print("Reprovado!")
media = (nota1 + nota2 + nota3) / 3
if media >= 9.5:
    print("Aprovado!")
elif media < 9.5:
    print("Reprovado!")
    


a = [3,2,1,5,4]
b = []

while a != []:
    ultima_letra = a.pop()
    b.append(ultima_letra)

print(b)

sair = False
while not sair:
    try:
        texto = input("Introduzir um  número")
        if texto == "sair":
            sair = True     
        else:
            numero = float(texto)
            numero += 50
    except ValueError:
        print("Devias ter metido um nmr")
