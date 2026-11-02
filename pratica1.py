PI = 3.14159
VELOCIDADE_LUZ = 299792458  # m/s

#Variaveis ex.
x = 10
nome = "Rodrigo Canelas"
altura = 1.83
ativo = True

#tipos de dados
print(type(PI))
print(type(VELOCIDADE_LUZ))
print(type(x))
print(type(nome))
print(type(altura))
print(type(ativo))

#4. Conversão explícita
a = "123"
type(a)  # <class 'str'>
b = int(a)
type(b)  # <class 'int'>
print(f"{a} é do tipo {type(a)}")
print(f"{b} é do tipo {type(b)}")   
#5. Operadores matemáticos
a = 10
b = 3
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

#6. Conversão implícita
print(f"{soma} temo {type(soma)}")
print(f"{subtracao} temo {type(subtracao)}")
print(f"{multiplicacao} temo {type(multiplicacao)}")
print(f"{divisao} temo {type(divisao)}")

