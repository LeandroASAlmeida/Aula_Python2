# VOCÊ FOI CONTRATADO PARA EFETUAR UM SISTEMA PARA UM POSTO DE COMBUSTÍVEIS
# PARA TANTO, DEVERÁ PEDIR O NOME DO MOTORISTA,
# TAMBÉM DEVERÁ INFORMAR O COMBUSTÍVEL DESEJADO
# [ETANOL, GASOLINA ADITIVADA, GASOLINA COMUM, DIESEL] COM OS RESPECTIVOS VALORES
# [4.689, 5.899, 7.099, 4.599]
# O SISTEMA DEVERÁ PERGUNTAR SE O MOTORISTA DESEJA INFORMAR O VALOR A PAGAR OU A QUANTIDADE DE LITROS
# CASO OPTE POR INFORMAR O VALOR, DEVERÁ PERGUNTAR QUANTO DESEJA PAGAR E RETORNAR OS LITROS ABASTECIDOS
# CASO OPTE POR INFORMAR OS LITROS, DEVERÁ PERGUNTAR QUANTOS LITROS E RETORNAR O VALOR A PAGAR

nome = input('Informe o nome do motorista: ')
op1 = int(input('Opção desejada: \n' + 
                '1- Valor a ser abastecido \n' + 
                '2- Litros a serem abastecido' ))
match op1:
    case 1:
        valor = float(input('Qual valor deseja abastecer? '))
        op2 = int(input('Combustível desejado: \n' + 
                        '----------------------------\n' + 
                        '1- Etanol  | 2- Gasolina Comum \n' + 
                        '3- Díesel  | 4- Gasolina Aditivada \n' + 
                        '----------------------------\n'))
        match op2:
            case 1:
                print('Volume abastecido: ' + str(valor / 4.689))
            case 2:
                print('Volume abastecido: ' + str(valor / 5.899))
            case 3:
                print('Volume abastecido: ' + str(valor / 4.599))
            case 4:
                print('Volume abastecido: ' + str(valor / 7.099))
            case outrocaso:
                print('Opção inválida')
    case 2:
        litros = float(input('Quantos litros deseja abastecer? '))
        op2 = int(input('Combustível desejado: \n' + 
                        '----------------------------\n' + 
                        '1- Etanol  | 2- Gasolina Comum \n' + 
                        '3- Díesel  | 4- Gasolina Aditivada \n' + 
                        '----------------------------\n'))
        match op2:
            case 1:
                print('Total a pagar: ' + str(litros * 4.689))
            case 2:
                print('Total a pagar: ' + str(litros * 5.899))
            case 3:
                print('Total a pagar: ' + str(litros * 4.599))
            case 4:
                print('Total a pagar: ' + str(litros * 7.099))
            case outrocaso:
                print('Opção inválida')
      
