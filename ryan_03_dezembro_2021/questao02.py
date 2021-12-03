# Autor: Wanderson Gomes da Costa
# E-mail: wanderson.gomes.costa05@aluno.ifce.edu.br
# Data da Ultima Modificacao: 03 de Dezembro de 2021

# PROBLEMA:
"""
    Um novo circo esta na cidade e fara uma promocao na
    semana de estreia, na qual o valor do ingresso tera
    um desconto de acordo com a faixa etaria do cliente:

    * 0 a 5 anos: 10% de desconto
    * 6 a 12 anos: 8% de desconto
    * 13 a 25 anos: 5% de desconto
    * Acima de 60 anos: 15% de desconto

    O valor normal do ingresso e de R$ 20.00. O dono do 
    circo percebeu que houve uma reducao no numero de clientes
    por espetaculo e decidiu continuar com a promocao da semana
    da estreia e divulgou a possibilidade de compra de ingressos
    em combo. Com isso, alem de solicitar o nome e a idade de cada
    cliente, o programa deve solicitar a quantidade de ingressos 
    (alem do cliente) do seu combo. O sistema deve solicitar o nome
    a idade das pessoas que irao com o cliente para o circo (0.4).
    O sistma deve aplicar os descontos abaixo no ingresso do cliente
    que indicou a opcao de combo:

    * 01 ingresso adicional: 25% de desconto (no ingresso do cliente)
    * 02 ingressos adicionais: 50% de desconto (no ingresso do cliente)
    * 03 ingressos adicionais: 75% de desconto (no ingresso do cliente)
    * 04 ou mais ingressos adicionais: 100% de desconto (no ingresso
    do cliente)
    
    O desconto do combo e cumulativo ao desconto de faixa etaria.

    Ao final o sistema deve gerar as seguintes informacoes:

    a) A relacao nominal dos clientes com 100% de desconto combom no
    seu ingresso;
    b) A quantidade de ingressos adicionais que foram comprados;
    c) O percentual de clientes que tiveram desconto combo de 50%;
    d) A media do valor de ingressos pagos por clientes com combo (
    considerando apenas o ingresso do cliente)
"""
# lista de clientes
clientes = []
qtd_clientes_desconto_cinquenta_combo = 0
total_ingressos_combo = 0

while True:
    #menu
    opcao = -1
    while opcao != 0 and opcao != 1:
        print("Deseja cadastrar outro cliente?")
        print("1 - SIM")
        print("0 - SAIR")
        opcao = int(input("Opcao: "))
        # error
        if opcao != 1 and opcao != 0:
            print("ERROR: opcao invalida! Tente novamente.")
    
    # sair do cadastro
    if opcao == 0:
        break
    else:
        # lendo os dados do cliente a ser cadastrado
        nome = input("Informe o nome do cliente: ")

        idade = -1
        while idade < 0:
            idade = int(input("Informe a idade do cliente: "))
            #error
            if idade < 0:
                print("ERROR: idade invalida! Tente novamente.")
        
        # quantidade de ingressos alem do cliente
        qtd_ingressos_alem = -1
        while qtd_ingressos_alem < 0:
            qtd_ingressos_alem = int(input("Informe a quantidade de ingressos alem do ingresso do cliente: "))
            if qtd_ingressos_alem < 0:
                print("ERROR: quantidade invalida! Tente novamente.")
        total_ingressos_combo += qtd_ingressos_alem

        valor_ingresso = 20.00

        # calcula o desconto
        desconto = 0.00
        if idade >= 0 and idade <= 5:
            desconto = valor_ingresso * 0.10 # 10%
        elif idade >= 6 and idade <= 12:
            desconto = valor_ingresso * 0.08 # 8%
        elif idade >= 13 and idade <= 25:
            desconto = valor_ingresso * 0.05 # 5%
        elif idade > 60:
            desconto = valor_ingresso * 0.15 # 15%
        
        # combo
        # verifica se ganhou algum combo
        combo = False
        if qtd_ingressos_alem > 0:
            combo = True
 
        if qtd_ingressos_alem == 1:
            desconto += valor_ingresso * 0.25 # 25%
        elif qtd_ingressos_alem == 2:
            qtd_clientes_desconto_cinquenta_combo += 1
            desconto += valor_ingresso * 0.50 # 50%
        elif qtd_ingressos_alem == 3:
            desconto += valor_ingresso * 0.75 # 75%
        elif qtd_ingressos_alem >= 4:
            desconto = valor_ingresso # 100%

        valor_pago = valor_ingresso - desconto

        # cadastra o cliente na lista
        clientes.append([nome, idade, valor_ingresso, desconto, valor_pago, combo])

# linha em branco
print()

# apresenta os dados solicitados
print("CLIENTES COM 100% DE DESCONTO:")
for cliente in clientes:
    if cliente[4] == 0:
        print(f'Nome: {cliente[0]}')

# apresenta a quantidade de ingressos adicionais
print(f'A QUANTIDADE DE INGRESSOS ADICIONAIS COMPRADOS FOI: {total_ingressos_combo}')

# apresenta a quantidade de clientes que tiveram desconto combo 50%
print(f'A quantidade de clientes que obteram desconto combo de 50%: {qtd_clientes_desconto_cinquenta_combo}')

# percentual de clientes que tiveram desconto combo de 50%
print(f'O percentual de clientes com desconto combo de 50%: {(qtd_clientes_desconto_cinquenta_combo/total_ingressos_combo) * 100:.2f} %')

# calcula a media do valor de ingressos pagos por clientes com combo
soma_ingressos_combo = 0.00
qtd_ingressos_combo = 0
for cliente in clientes:
    if cliente[5] == True:
        soma_ingressos_combo += cliente[4]
        qtd_ingressos_combo += 1

if qtd_ingressos_combo > 0:
    media = soma_ingressos_combo/qtd_ingressos_combo

print(f'A MEDIA do preco dos ingressos pagos com desconto combo e: {media}')