# Exercício 29
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('A velocidade do carro em Km/h é: '))

if vel > 80 :
    m = (vel - 80) * 7
    print('Acima da velocidade permitida! Recebeu uma multa no valor de {}'.format(m))
