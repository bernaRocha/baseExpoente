#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

base = int(input("Digite o número da base: "))
expoente = int(input("Digite a potência: "))

resultado = base ** expoente

print("Tendo como base de {} e potência de {}, o resultado é {}.".format(base, expoente, resultado))