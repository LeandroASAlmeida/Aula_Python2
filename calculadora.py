#Elabore uma calculadora onde o usuário informa 2 valores inteiros
#devera selecionar a operação desejada[+ - * /] e retorne o resultado de acordo com a opção
#ULTILIZAR CASE

num1 = int(input('INFORME UM NUMERO: '))
num2 = int(input('INFORME OUTRO NUMERO: '))
op = int(input('SELECIONE UMA DAS OPÇÕES: [ +   -   *   / ]'))

match op:
    case ("+"):
        print('A soma  é :' + str(num1 + num2))
    case ("-"):
        print('A subtração  é :' +str(num1 - num2))
    case ("*"):
        print('A multiplicação  é :' + str(num1 * num2))
    case ("/"):
         if (num2 == 0):
           print('Impossivel dividir por zero')
         else:
           print('A divisão  é :' + str(num1 / num2))
    case outrocaso:
        print('Op INvalida')