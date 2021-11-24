# Autor: Wanderson Gomes da Costa
# E-mail: wanderson.gomes.costa05@aluno.ifce.edu.br
# Data da Ultima Modificao: 24 de Novembro de 2021

# dados
desconto = 0.00
valor_consulta = 0.00

qtd_clinico_geral = 0
qtd_nutriconista = 0
qtd_fonoaudiologo = 0
qtd_fisioterapeuta = 0
qtd_odontologo = 0

total_clientes_atendidos = 0

lista_clientes_convenio_acima_59 = []

total_apurado = 0.00

# constantes
PORCENTAGEM_DESCONTO = 0.75 # 75 %

CLINICO_GERAL = 1
NUTRICIONISTA = 2
FONOAUDIOLOGO = 3
FISIOTERAPEUTA = 4
ODONTOLOGO = 5

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
            qtd_clinico_geral += 1
        elif opcao_atendimento == NUTRICIONISTA:
            valor_consulta = 150.00
            qtd_nutriconista += 1
        elif opcao_atendimento == FONOAUDIOLOGO:
            valor_consulta = 200.00
            qtd_fonoaudiologo += 1
        elif opcao_atendimento == FISIOTERAPEUTA:
            valor_consulta = 150.00
            qtd_fisioterapeuta += 1
        elif opcao_atendimento == ODONTOLOGO:
            valor_consulta = 200.00
            qtd_odontologo += 1
        
        # ATUALIZA A QUANTIDADE DE CLIENTES ATENDIDOS
        total_clientes_atendidos += 1

        # APLICACAO OU NAO DO DESCONTO E VERIFICAO SE TEM MAIS DE 59 ANOS
        # E ADICIONAR NA LISTA DE CLIENTES
        if tem_convenio == 's':
            desconto = valor_consulta * PORCENTAGEM_DESCONTO
            valor_consulta = valor_consulta - desconto

            if idade > 59:
                lista_clientes_convenio_acima_59.append(nome_cliente)

        # ATUALIZA O TOTAL APURADO
        total_apurado += valor_consulta
    else:
        break


# APRESENTACAO DO DADOS COLHIDOS NO EXPEDIENTE
print("\nQUANTIDADE DE ATENDIMENTOS")
print(f'Clinico Geral: {qtd_clinico_geral} atendimento(s)')
print(f'Nutricionista: {qtd_nutriconista} atendimento(s)')
print(f'Fonoaudiologo: {qtd_fonoaudiologo} atendimento(s)')
print(f'Fisioterapeuta: {qtd_fisioterapeuta} atendimento(s)')
print(f'Odontologo: {qtd_odontologo} atendimento(s)')

print("\nRELACAO NOMINAL DOS CLIENTES COM CONVENIO E IDADE ACIMA DE 59 ANOS:")
if len(lista_clientes_convenio_acima_59) > 0:
    for nome in lista_clientes_convenio_acima_59:
        print(nome)
else:
    print("Nenhum cliente satisfez os requisitos.")

percentual_fisioterapeuta = 0.00
if total_clientes_atendidos != 0:
    percentual_fisioterapeuta = (qtd_fisioterapeuta/total_clientes_atendidos) * 100

print(f'\nPERCENTUAL DE CLIENTES QUE REALIZARAM ATENDIMENTO COM UM FISIOTERAPEUTA: {percentual_fisioterapeuta:.2f} %')

print(f'\nO TOTAL ARRECADADO FOI DE R$ {total_apurado:.2f}')