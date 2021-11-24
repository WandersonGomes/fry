# Autor: Wanderson Gomes da Costa
# E-mail: wanderson.gomes.costa05@aluno.ifce.edu.br
# Data da Ultima Modificao: 24 de Novembro de 2021

# dados
lista_atendimentos = []

# constantes
PORCENTAGEM_DESCONTO = 0.75 # 75 %

CLINICO_GERAL = 1
NUTRICIONISTA = 2
FONOAUDIOLOGO = 3
FISIOTERAPEUTA = 4
ODONTOLOGO = 5

ESPECIALIDADE = 0
NUMERO_CPF = 1
NOME = 2
CONVENIO = 3
VALOR_CONSULTA_CLIENTE = 4
VALOR_DESCONTO_CONVENIO = 5

while True:
    # LEITURA DO CPF DO CLIENTE
    cpf = 0
    while cpf <= 0 and cpf != -1:
        cpf = int(input("\nInforme o CPF do cliente ou [-1] para encerrar o expediente: "))

        # error
        if cpf <= 0 and cpf != -1:
            print("Error: cpf invalido! Tente novamente.")

    # se for cpf valido continua o expediente
    if cpf != -1:
        # MENU DE ATENDIMENTO
        opcao_atendimento = 0
        while opcao_atendimento < 1 or opcao_atendimento > 5:
            print("\nMENU")
            print("1 - Clinico Geral")
            print("2 - Nutricionista")
            print("3 - Fonoaudiologo")
            print("4 - Fisioterapeuta")
            print("5 - Odontologo")
            opcao_atendimento = int(input("Informe o tipo de atendimento: "))

            #error
            if opcao_atendimento < 1 or opcao_atendimento > 5:
                print("Error: opcao invalida! Tente novamente.")

        # LEITURA DO NOME DO CLIENTE
        nome_cliente = input("\nInforme o nome do cliente: ")

        # LEITURA DA IDADE DO CLIENTE
        idade = -1
        while idade < 0:
            idade = int(input("\nInforme a idade do cliente (anos): "))

            # error
            if idade < 0:
                print("Error: idade invalida! Tente novamente.")

        # LEITURA SE O CLIENTE TEM CONVENIO
        tem_convenio = 'a'
        while tem_convenio != 's' and tem_convenio != 'n':
            tem_convenio = input("\nO cliente tem convenio? [s/n]: ")
            tem_convenio = tem_convenio.lower()[0]

            # error
            if tem_convenio != 's' and tem_convenio != 'n':
                print("Error: resposta invalida! Tente novamente.")

        # VERIFICA O VALOR DA CONSULTA E CONTA OS ATENDIMENTOS
        if opcao_atendimento == CLINICO_GERAL:
            valor_consulta = 250.00
        elif opcao_atendimento == NUTRICIONISTA:
            valor_consulta = 150.00
        elif opcao_atendimento == FONOAUDIOLOGO:
            valor_consulta = 200.00
        elif opcao_atendimento == FISIOTERAPEUTA:
            valor_consulta = 150.00
        elif opcao_atendimento == ODONTOLOGO:
            valor_consulta = 200.00
        
        # APLICACAO OU NAO DO DESCONTO E VERIFICAO SE TEM MAIS DE 59 ANOS
        # E ADICIONAR NA LISTA DE CLIENTES
        desconto = 0.00
        if tem_convenio == 's':
            desconto = valor_consulta * PORCENTAGEM_DESCONTO

        # ADICIONA A LISTA DE ATENDIMENTOS
        lista_atendimentos.append([opcao_atendimento, cpf, nome_cliente, tem_convenio, valor_consulta, desconto])

    else:
        break

# PROCESSAMENTO DOS DADOS RECEBIDOS
atendimento_especialidades = [0, 0, 0, 0, 0]
lista_clientes_convenio_acima_59 = []
total_arrecadado = 0.00

for atendimento in lista_atendimentos:
    # contagem de atendimento de cada especialidade
    if atendimento[ESPECIALIDADE] == CLINICO_GERAL:
        atendimento_especialidades[CLINICO_GERAL - 1] += 1
    elif atendimento[ESPECIALIDADE] == NUTRICIONISTA:
        atendimento_especialidades[NUTRICIONISTA - 1] += 1
    elif atendimento[ESPECIALIDADE] == FONOAUDIOLOGO:
        atendimento_especialidades[FONOAUDIOLOGO - 1] += 1
    elif atendimento[ESPECIALIDADE] == FISIOTERAPEUTA:
        atendimento_especialidades[FISIOTERAPEUTA - 1] += 1
    elif atendimento[ESPECIALIDADE] == ODONTOLOGO:
        atendimento_especialidades[ODONTOLOGO - 1] += 1
    
    # atualizacao da lista de atendimentos com convenio e acima de 59 anos
    if atendimento[CONVENIO] == 's':
        lista_clientes_convenio_acima_59.append(atendimento)

    # total arrecadado
    total_arrecadado += atendimento[VALOR_CONSULTA_CLIENTE] - atendimento[VALOR_DESCONTO_CONVENIO]

# APRESENTACAO DO DADOS COLHIDOS NO EXPEDIENTE
print("\nQUANTIDADE DE ATENDIMENTOS")
print(f'Clinico Geral: {atendimento_especialidades[CLINICO_GERAL - 1]} atendimento(s)')
print(f'Nutricionista: {atendimento_especialidades[NUTRICIONISTA - 1]} atendimento(s)')
print(f'Fonoaudiologo: {atendimento_especialidades[FONOAUDIOLOGO - 1]} atendimento(s)')
print(f'Fisioterapeuta: {atendimento_especialidades[FISIOTERAPEUTA - 1]} atendimento(s)')
print(f'Odontologo: {atendimento_especialidades[ODONTOLOGO - 1]} atendimento(s)')

print("\nRELACAO NOMINAL DOS CLIENTES COM CONVENIO E IDADE ACIMA DE 59 ANOS:")
if len(lista_clientes_convenio_acima_59) > 0:
    for cliente in lista_clientes_convenio_acima_59:
        print(cliente[NOME])
else:
    print("Nenhum cliente satisfez os requisitos.")

percentual_fisioterapeuta = 0.00
if len(lista_atendimentos) > 0:
    percentual_fisioterapeuta = (atendimento_especialidades[FISIOTERAPEUTA - 1]/len(lista_atendimentos)) * 100

print(f'\nPERCENTUAL DE CLIENTES QUE REALIZARAM ATENDIMENTO COM UM FISIOTERAPEUTA: {percentual_fisioterapeuta:.2f} %')

print(f'\nO TOTAL ARRECADADO FOI DE R$ {total_arrecadado:.2f}')