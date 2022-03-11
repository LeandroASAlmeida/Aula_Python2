# Para ingressar no Exército Brasileiro como soldado, a pessoa deverá obedecer os seguintes 
# requisitos. [Ter idade de 18 anos E ser do sexo masculino]
# Implemente um algoritmo que peça o nome, idade e sexo da pessoa 
# e diga se esta está CONVOCADA ou DISPENSADA do serviço militar
# UTILIZAR CASE PARA O SEXO E IDADE

nome = input('QUAL É O SEU NOME: ')
sexo = input('QUAL SEU SEXO= [M]MASCULINO OU [F]FEMININO: ')

match sexo.upper():
    case 'M':
        idade = int(input('Informe a idade ' + nome + ': '))
        match idade:
            case 18:
                print('CONVOCADO')
            case outrocaso:
                print('DISPENSADO')
    case outrocaso:
        print("DINPENSADA")
