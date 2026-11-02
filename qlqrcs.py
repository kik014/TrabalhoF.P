print("Bem vindo ao nosso site!")
input("Pressione enter para continuar...")
idade = float(input("Digite a sua idade para começar:"))
if idade < 18:
    print("Não pode é válido a sua entrada.")
else:
    print("A sua idade foi validada")

# Número secreto que o utilizador tem de adivinhar
numero_secreto = 7

print("Bem-vindo ao jogo da adivinhação!")

while True:
    try:
        # 1. Pede o número ao utilizador e converte para inteiro
        palpite = int(input("Adivinha um número entre 1 e 10: "))
        
        # 2. Verifica se o número está correto
        if palpite == numero_secreto:
            print("Parabéns! Acertaste no número secreto! 🎉")
            break  # Termina o ciclo while
        elif palpite < numero_secreto:
            print("O número secreto é maior. Tenta outra vez!")
        else:
            print("O número secreto é menor. Tenta outra vez!")
            
    except ValueError:
        # 3. Tratamento de erro caso o utilizador escreva letras ou deixe vazio
        print("Erro: Tens de introduzir um número inteiro válido (por exemplo, 5).")

numeros = []
print("Por favor selecione 5 numeros:")
for i in range(5):
    valor = int(input(f"Números{i+1}"))
    numeros.append(valor)
maior_numero = max(numeros)
print(f"O maior nº que selecionaste foi: {maior_numero}")

nota = int(input("Digite a sua nota:"))
if nota >= 10:
    print("Parabéns passaste!")
elif nota < 10:
    print("Reprovaste tens de estudar mais...")

soma_total = 0
print("Introduza 5 nºs:")
for i in range(5):
    numero = float(input(f"Introduza o {i+1}º numeros:"))
    soma_total = soma_total + numero
print(" A soma total dos 5 nºs é", soma_total)
