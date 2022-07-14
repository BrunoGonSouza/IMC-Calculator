'''Universidade cruzeiro do sul
   Bruno Gonçalves de souza
   02/04/2022
   Exercício 11 - Construa um programa para determinar se o indivíduo está
   com um peso favorável. Essa situação é determinada através do IMC
   (Índice de Massa Corpórea), que é definida como sendo a relação entre o peso 
   (PESO) e o quadrado da Altura (ALTURA) do indivíduo de acordo com a
   equação e tabela ao lado:'''

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura (ex:1.70): "))

imc = peso / altura**2

print(f"Seu Índice de massa corpórea é: {imc:.1f}")

if imc < 20:
    print("Abaixo do peso")
elif imc >= 20 and imc <25:
    print("Peso normal")
elif imc >= 25 and imc <30:
    print("Sobrepeso")
elif imc >= 30 and imc <40:
    print("Obeso")
elif imc >= 40:
    print("Obeso Mórbido")

