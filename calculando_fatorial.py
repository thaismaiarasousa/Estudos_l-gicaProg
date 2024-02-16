numero = int(input('Digite um número: '))
if numero > 0:
    fatorial = 1
    for item in range (1, numero +1):
        fatorial *= item
    print(fatorial)