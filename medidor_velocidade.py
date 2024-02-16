velocidade =int(input('Digite sua velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('Sem multas em seu nome!')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('Você obteve uma multa leve.')
elif velocidade > velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Você obteve uma multa grave.')
elif velocidade > velocidade_maxima + 20:
    print('Você obteve uma multa gravíssima.')
    
   