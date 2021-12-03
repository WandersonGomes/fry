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
    circo deseja controlar a venda de ingressos e por isso
    solicitou a uma empresa de TI que faca um programa em
    PYTHON utilizando listas, que, para cada cliente, soli-
    cite o nome e idade, e ao final gere as informacoes
    abaixo:

    a) A relacao dos clientes, idade e o valor do ingresso
    pago.
    b) A quantidade de clientes que nao tiveram desconto.
    c) O percentual de clientes que tiveram desconto de 8%.
    d) A relacao dos clientes que possuem acima de 60 anos.
    e) A media do valor de descontos aplicados.
"""
# lista de clientes
clientes = []
qtd_clientes_desconto_oito = 0

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
        
        valor_ingresso = 20.00

        desconto = 0.00
        if idade >= 0 and idade <= 5:
            desconto = valor_ingresso * 0.10 # 10%
        elif idade >= 6 and idade <= 12:
            qtd_clientes_desconto_oito += 1
            desconto = valor_ingresso * 0.08 # 8%
        elif idade >= 13 and idade <= 25:
            desconto = valor_ingresso * 0.05 # 5%
        elif idade > 60:
            desconto = valor_ingresso * 0.15 # 15%

        valor_pago = valor_ingresso - desconto

        # cadastra o cliente na lista
        clientes.append([nome, idade, valor_ingresso, desconto, valor_pago])

# linha em branco
print()

# apresenta os dados solicitados
print("CLIENTES:")
for cliente in clientes:
    print(f'Nome: {cliente[0]}, Idade: {cliente[1]}, Valor Normal do Ingresso: {cliente[2]}, Desconto por Faixa Etaria: {cliente[3]}, Valor Pago: {cliente[4]}')

# calcula a quantidade de clientes sem desconto
qtd_sem_desconto = 0
for cliente in clientes:
    if cliente[3] == 0:
        qtd_sem_desconto += 1
print(f'QUANTIDADE SEM DESCONTO: {qtd_sem_desconto}')

# calcula o percentual de clientes que tiveram desconto de 8%
if len(clientes) > 0:
    print(f'PERCENTUAL DE CLIENTES COM DESCONTO DE 8%: {(qtd_clientes_desconto_oito/len(clientes)):.2f) * 100} %')

# apresenta a relacao dos clientes que possuem acima de 60 anos
print("CLIENTES COM IDADE ACIMA DE 60 ANOS:")
for cliente in clientes:
    if cliente[1] > 60:
        print(f'Nome: {cliente[0]}, Idade: {cliente[1]}, Valor Normal do Ingresso: {cliente[2]}, Desconto por Faixa Etaria: {cliente[3]}, Valor Pago: {cliente[4]}')

# calcula a media de valores de descontos aplicados
soma_descontos = 0.00
for cliente in clientes:
    soma_descontos += cliente[3]

if (len(clientes) > 0):
    print(f'MEDIA DO VALOR DE DESCONTO APLICADO: {soma_descontos/len(clientes):.2f}')