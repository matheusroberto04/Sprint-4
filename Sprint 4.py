# Importando bibliotecas necessarias
import cx_Oracle as oc
import pandas as pd
import requests
# Menu de escolha que retorna um valor para inicializar uma funçoes do menu
def exibir_menu():
    escolha = (input('''
=================================================
                BIKE CHECK
               ᴾᵒʳᵗᵒ ˢᵉᵍᵘʳᵒ
=================================================
    MENU: 
    |------------------------------------------|
    | [1] - Vistoria de Bike                   |
    | [2] - Cadastro de usuario                |
    | [3] - Menu de Informações(FAQ)           |
    | [4] - Sair                               |             
    | [5] - GitHub dos DEVS                    |
    |------------------------------------------|
    ---> '''))
    return escolha

# Lista de dicionario que armazenara dados das funções <dados_pessoais():>, <dados_de_contato()> e <captura_dados_endereço()>
dados_usuario = None

# Funçao que guarda menu de informações
# Respostas fornecidas do site da Posto Seguro
def exibir_informacoes():
    
    escolha_faq = 0

    while escolha_faq != 6:
        print('''       =================================================
                Bem-vindo ao menu de informações!

                Por favor, selecione a opção desejada!
           ===================================================
        ''')
        print('''
        [1] -> Quais os benefícios de ter o nosso seguro?
        [2] -> Como faço para contratar um seguro?
        [3] -> O seguro de bike cobre danos acidentais?
        [4] -> Existe um limite de idade ou modelo da bicicleta para obter o seguro?
        [5] -> O que fazer em caso de roubo da bicicleta segurada?
        [6] -> Sair.
        ''')
        escolha_faq = int(input("Escolha uma opção: "))

        if escolha_faq == 1:
            print(''' 
                Com o nosso seguro, você terá diversos benefícios como:
                -> Desconto de 5% na contratação de mais de uma bike em uma única apólice.
                -> Seguro de vida, caso haja alguma morte acidental ou invalidez permanente decorrente do acidente.
                -> Cobrimos as despesas médicas, hospitalares e odontológicas, caso o cliente se envolva em um acidente.
                -> Cobre o extravio da bicicleta em viagens aéreas ou rodoviárias, durante o trajeto de ida e volta, 
                desde que esteja com o ticket de embarque.

                -> Pedal Essencial: plano gratuito que oferece reparo e/ou troca de câmaras de ar, correntes, coroas, 
                manetes de freios, além de lubrificação de correntes.

                -> Pedal Leve: mesmas garantias do plano Pedal Essencial, com um benefício a mais: transporte do 
                segurado e sua bike em caso de quebra ou acidente, com limite de 50 km.

                -> Pedal Elite: Tem tudo o que o plano Pedal Essencial oferece, com um benefício a mais: transporte 
                do segurado e sua bike em caso de quebra ou acidente, com limite de 150 km.                  
            ''')

        elif escolha_faq == 2:
            print('''
            Para contratar o nosso serviço, basta entrar em contato com os nossos atendentes através do 
            nosso site ou pelo WhatsApp 11 3003 9303!
            ''')

        elif escolha_faq == 3:
            print(''' Sim! Cobrimos danos como:
                -> Incêndio
                -> Queda
                -> Tentativa de roubo
                -> Situações em que a bicicleta esteja sendo transportada por um veículo.
                -> Situação de curto-circuito em bikes elétricas.
            ''')

        elif escolha_faq == 4:
            print(''' 
                O cliente deve ser maior de 18 anos, além de necessitar ter em mãos a nota fiscal da bicicleta, 
                principalmente se for comprada no exterior, e a bike deve ser:
                -> Tradicional/nova.
                -> Tradicional com até 8 anos de uso.
                -> Bicicleta elétrica com até 3 anos de uso.
            ''')

        elif escolha_faq == 5:
            print(''' 
            Caso a sua bicicleta seja roubada, você deve entrar em contato através do nosso site ou 
            WhatsApp 11 3003 9303. No entanto, em caso de furto simples, como o desaparecimento da bicicleta ou roubo sem 
            vestígios, não são cobertos pelo seguro bike.
            ''')

        elif escolha_faq == 6:
            print('Obrigado por escolher o nosso seguro, a Porto agradece!')
            break

        else:
            print('Opção inválida')

        escolha = int(input("\nPressione [1] - Para voltar ao menu de informações - [2] Para sair: "))
        if escolha == 1:
            escolha_faq = 0
        else:
            escolha_faq = 6

# Função que recebe e armazena os dados pessoais
def dados_pessoais():
    sair = 1
    while sair == 1:
        print('''
        ==== DADOS PESSOAIS ====
        ''')
        nome_completo = input('Nome completo: ')
        nascimento = input('Data de nascimento( No formato 10/10/1999 ): ')
        # Extrai o ano de nascimento com a utilização do metodo .split e dividirá a data em partes com base na barra '/'
        ano_nascimento = int(nascimento.split("/")[-1])
        # Condição que confirma se o usuario é menor de idade
        if ano_nascimento > 2004:
            sair = 0
        else:
            print('//Você está apto para adquirir o seguro da Porto!')
        cpf = input('Informe seu CPF( No formato 000.000.000 - 00): ')
        sexo = input('Sexo( M/F ): ')
        # Utilizando API pandas para criar tabelas, para que o cliente tenha uma melhor visao para confirmacao
        print('='*50)
        dados = [ 
        {'|Nome|': nome_completo, '|Nascimento|': nascimento, '|CPF|': cpf, '|Sexo|': sexo},]
        dados = pd.DataFrame(dados)
        print(dados)
        print('='*50)
         # Variavel que será utilizada para sair do loop
        confirmacao = int(input('Confirma as informações? [1] SIM, [2] NÃO\n'))
        # Armazena os valores das variáveis no dicionário
        dados_pessoais = {
            'Nome': nome_completo,
            'Idade': ano_nascimento,
            'CPF': cpf,
            'Sexo': sexo
        }
        print('--------------------------------')
        m = 0
        # Verifica se algum elemento do dicionario esta vazio caso o usuário tenha deixando algum input em branco
        for i in dados_pessoais:
            if dados_pessoais[i] == '':
                print(f'{i}: campo vazio, preencha novamente!')
                m += 1
        # A variavel <m> é utilizado como verificador caso uma Chave esteja com valor nulo para continuar com o loop
        if m > 0:
            sair = 1
        elif confirmacao == 1:
            print('Obrigado por confirmar seus dados pessoais!')
            sair = 0
        elif confirmacao != 2:
            print('Opção Inválida!')

    return dados_pessoais, ano_nascimento

# Função que recebe e armazena os dados de contato
def dados_de_contato():
    sair = 1
    while sair == 1:
        print('''
            ==== CONTATO ====
            ''')
        email_usuario = input('Informe seu e-mail (ex: examplo@gmail.com): ')
        telefone = input('Informe seu telefone (Residencial ou Celular): ')
        # API pandas usada para formar tabela, para melhor confirmacao visual do cliente
        print('='*50)
        tabela_dados = [
            {'|Email|': email_usuario, '|Telefone|': telefone}
        ]
        tabela_dados = pd.DataFrame(tabela_dados)
        print(tabela_dados)
        print('='*50)
        # Variavel que será utilizada para sair do loop
        confirmacao = int(input('Confirma as informações? [1] SIM, [2] NÃO\n'))
        # Armazena os valores das variáveis no dicionário
        contato = {
            'E-mail': email_usuario,
            'Telefone': telefone,
        }
        print('--------------------------------')
        m = 0
        # Verifica se algum elemento do dicionario esta vazio caso o usuário tenha deixando algum input em branco
        for i in contato:
            if contato[i] == '':
                print(f'{i}: campo vazio, preencha novamente!')
                m += 1
        # A variavel <m> é utilizado como verificador caso uma Chave esteja com valor nulo para continuar com o loop
        if m > 0:
            sair = 1
        elif confirmacao == 1:
            print('Obrigado por confirmar seus dados de contanto!')
            sair = 0
        elif confirmacao != 2:
            print('Opção Inválida!')
    return contato

# Função que recebe e armazena o endereço do usuário
def captura_dados_endereço():
    print('==== ENDEREÇO ====')
    sair = 1
    while sair == 1:
        cep = input('CEP: ')
        #API de localizacao!
        cep = cep.replace("-","")
        if len(cep) == 8:
            link = f'https://viacep.com.br/ws/{cep}/json/'

            requisicao = requests.get(link)
            print(requisicao)

            dic_requisicao = requisicao.json()
            print(dic_requisicao)

            uf = dic_requisicao['uf']
            cidade = dic_requisicao['localidade']
            bairro = dic_requisicao['bairro']
            rua = dic_requisicao['logradouro']
            print(f'Cidade: {cidade}')
            print(f'Estado: {uf}')
            print(f'Bairro: {bairro}')
            print(f'Rua: {rua}')
        else:
            print('CEP invalido!')
        complemento = input('Informe um complemento (Ex: Apto 1 Bloco A e/ou numero da residencia): ')
        # API pandas mais uma vez sendo usada para criar tabela
        print('='*70)
        tabela_endereco = [
            {'|Estado|':  uf ,'|Cidade|': cidade, '|Bairro|': bairro, '|Rua|': rua,'|CEP|': cep , '|Complemento|': complemento}
        ]
        tabela_endereco = pd.DataFrame(tabela_endereco)
        print(tabela_endereco)
        print('='*70)
         # Variavel que será utilizada para sair do loop
        confirmacao = int(input('Confirma as informações? [1] SIM, [2] NÃO\n'))
        # Armazena os valores das variáveis no dicionário
        dados_endereco = {
            'Rua': rua,
            'Cidade': cidade,
            'CEP': cep,
            'Complemento': complemento
        }
        m = 0
        print('-------------------------------------')
        # Verifica se algum Valor do dicionario esta vazio caso o usuário tenha deixando algum input em branco
        for i in dados_endereco:
            if dados_endereco[i] == '':
                print(f'{i}: campo vazio, preencha novamente!')
                m += 1
        # A variavel <m> é utilizado como verificador caso uma Chave esteja com valor nulo para continuar com o loop
        if m > 0:
            sair = 1
        elif confirmacao == 1:
            print('Obrigado por confirmar seu endereço!')
            sair = 0
        elif confirmacao != 2:
            print('Opção Inválida!')

    return dados_endereco

#-----------------------------------------------------------------------------------------#
# Função que recebe e armazena o componentes da bicicleta
def capturar_componentes_bike():
    ponto_positivos = 0
    ponto_negativos = 0
    print('======================')
    print('Componentes Da Bike')
    print('======================')
    sair = 1
    while sair == 1 :
        print('\n== Pneus ==  ')
        pneus = input('estado: Novo, Usado, Furados: \n').lower()
        if pneus == 'novo':
            ponto_positivos += 1
            break
        elif pneus == 'usado':
            ponto_negativos += 1
            break
        elif pneus == 'furados':
            ponto_negativos += 2
            break
        else:
            print('Opção Inválida!')
            print('------------------')

    while True:
        print('\n== Freios ==  ')
        freios = input('Estado: novo, desgastadas: \n').lower()
        if freios == 'novo':
            ponto_positivos += 1
            break
        elif freios == 'desgastadas':
            ponto_negativos += 1
            break
        else:
            print('------------------')
            print('Opção Inválida!')
            print('------------------')

    while True:
        print('\n== Suspenção(se aplicável) ==  ')
        suspencao = input('Estado: Boa, Com Problemas, Não Aplicável: \n').lower()
        if suspencao == 'boa':
            ponto_positivos += 1
            break
        elif suspencao == 'com problemas' or suspencao == 'problemas':
            ponto_negativos += 1
            break
        elif suspencao == 'nao' or suspencao == 'não' or suspencao == 'não aplicável' or suspencao == 'nao aplicavel':
            ponto_negativos += 1
            break
        else:
            print('------------------')
            print('Opção Inválida!')
            print('------------------')

    while True:
        print('\n== Quadro e Garfo ==  ')
        quadro_e_garfo = input('Integridade Estrutural: Boa, Com Rachaduras, Danos: \n').lower()
        if quadro_e_garfo == 'boa' or quadro_e_garfo == '1':
            ponto_positivos += 1
            break
        elif quadro_e_garfo == 'com rachaduras' or quadro_e_garfo == 'rachaduras':
            ponto_negativos += 1
            break
        elif quadro_e_garfo == 'danos':
            ponto_positivos += 2
            break
        else:
            print('------------------')
            print('Opção Inválida!')
            print('------------------')

    while True:
        print('\n== Manoplas ==  ')
        manoplas = input('Estado: Novas, Desgastadas:  \n').lower()
        if manoplas == 'novas':
            ponto_positivos += 1
            break
        elif manoplas == 'desgastadas':
            ponto_negativos += 1
            break
        else:
            print('------------------')
            print('Opção Inválida!')
            print('------------------')

    while True:
        print('\n== Sistema de Transmissão ==  ')
        while True:
            marchas_e_cambios = input('Marchas e Câmbios: Funcionando Adequadamente, Com Problemas: \n').lower()
            if marchas_e_cambios == 'funcionando' or marchas_e_cambios == 'funcionando adequadamente':
                ponto_positivos += 1
                break
            elif marchas_e_cambios == 'com problemas' or marchas_e_cambios == 'problemas':
                ponto_negativos += 1
                break
            else:
                print('------------------')
                print('Opção Inválida!')
                print('------------------')
        sistema_de_transmissão = input('Corrente: Nova, Desgastada: \n').lower()
        if sistema_de_transmissão == 'nova':
            ponto_positivos += 1
            break
        elif sistema_de_transmissão == 'desgastada':
            ponto_negativos += 1
            break
        else:
            print('------------------')
            print('Opção Inválida!')
            print('------------------')

    while True:
        print('\n== Sistema de Iluminação e sinalização (se aplicável) ==  ')
        sistema_iluminacao = input(
            'Funcionando (para luzes dianteira e traseira): Sim , Não, Não se aplica: \n').lower()
        if sistema_iluminacao == 'sim':
            ponto_positivos += 2
            break
        elif sistema_iluminacao == 'nao' or sistema_iluminacao == 'não':
            ponto_negativos += 1
            break
        elif sistema_iluminacao == 'não se aplica' or sistema_iluminacao == 'nao se aplica':
            ponto_negativos += 1
        else:
            print('------------------')
            print('Opção Inválida!')
            print('------------------')

    while True:
        print('\n== Campainha ==  ')
        campainha = input('Funcionando: Sim, Não: \n').lower()
        if campainha == 'sim':
            ponto_positivos += 1
            break
        elif campainha == 'não' or campainha == 'nao':
            ponto_negativos += 1
            break
        else:
            print('------------------')
            print('Opção Inválida!')
            print('------------------')
        # API pandas novamente
    print('='*50)
    tabela_componente = [
        {'|Pneus|': pneus, '|Freio|': freios,'|Marchas e Cambios|': marchas_e_cambios}
    ]
    tabela_componente = pd.DataFrame(tabela_componente)
    print(tabela_componente)
    print('='*50)
    #
    tabela_componente2 = [
        {'|Quadro e garfo|': quadro_e_garfo, 'Manoplas|': manoplas}
    ]
    tabela_componente2 = pd.DataFrame(tabela_componente2)
    print(tabela_componente2)
    print('='*50)
    tabela_componente4 = [
        {'|Sistemas de transmissao|': sistema_de_transmissão, '|Suspencao|': suspencao}
    ]
    tabela_componente4 = pd.DataFrame(tabela_componente4)
    print(tabela_componente4)
    print('='*50)
    tabela_componente5 = [
         {'|Campainha|': campainha, '|Sistema de iluminacao|': sistema_iluminacao}
    ]
    tabela_componente5 = pd.DataFrame(tabela_componente5)
    print(tabela_componente5)
    print('='*50)
     # Variavel que será utilizada para sair do loop
    confirmacao = int(input('Confirma as informações? [1] SIM, [2] NÃO\n'))
    if confirmacao == 1:
        print("\nInformações Confirmadas\n")
    elif confirmacao == 2:
        print("\n Os dados foram cancelados\n")
        capturar_componentes_bike()
    componentes_bike = {
        'Pneu': pneus,
        'Freios': freios,
        'Suspenção': suspencao,
        'Garfo': quadro_e_garfo,
        'Manoplas': manoplas,
        'Sistema de Transmissão': sistema_de_transmissão,
        'Sistema de sinalização': sistema_iluminacao,
        'Campainha': campainha,
    }

    # As variáveis <ponto_positivos> e <ponto_negativos> serão usadas para validar a vistoria na função <menu()>
    return ponto_positivos, ponto_negativos, componentes_bike

# Função que recebe e armazena o informações importantes da bike
def criar_registro_bike():
    print('='*20)
    print('Registro de Bike')
    print('=' * 20)
    sair = 1
    while sair == 1 :
        numero_serie = input('Informe o Número de Série (ex: 3R27U85549): ')
        if numero_serie == '':
            print('...')
        else:
            break
    while True:
        marca_bike = input('Informe a Marca da Bike: ')
        if marca_bike == '':
            print('...')
        else:
            break
    while True:
        modelo_bike = input('Informe o Modelo da Bike: ')
        if modelo_bike == '':
            print('...')
        else:
            break
    while True:
        valor_bike = float(input('Informe o Valor da Bike: R$'))
        if valor_bike < 0:
            print('O valor não pode ser negativo!')
        else:
            break
    # API pandas de tabela
    print('='*70)
    tabela_registro_bike = [
        {'|Numero de serie|': numero_serie,'|Marca|': marca_bike, '|Modelo da bike|': modelo_bike,'|Valor da bike|': valor_bike}
    ]
    tabela_registro_bike = pd.DataFrame(tabela_registro_bike)
    print(tabela_registro_bike)
    print('='*70)
    # Variavel que será utilizada para sair do loop
    confirmacao = int(input('Confirma as informações? [1] SIM, [2] NÃO\n'))   
    if confirmacao == 1:
        print('\nDados registrados com sucesso!\n')
    elif confirmacao == 2:
        print('\nOs dados foram cancelados.\n')
        criar_registro_bike()
    registro_bike = {
        'Num Série': numero_serie,
        'Marca': marca_bike,
        'Modelo': modelo_bike,
        'Valor': valor_bike
    }
    print('-------------------------------------')
    # As variáveis <ponto_positivos> e <ponto_negativos> serão usadas para validar a vistoria na função <menu()>
    return registro_bike

# Função que recebe e armazena o recursos de segurança da bike
def recursos_de_seguranca_bike():
    print('=' * 25)
    print('Recursos de Segurança')
    print('=' * 25)
    ponto_positivo = 0
    ponto_negativo = 0
    sair = 1
    while sair == 1 :
        print('\n== Travas de Segurança ==')
        trava_seguranca = input('Você tem: Sim, Não --> \n').lower()
        if trava_seguranca == 'sim':
            ponto_positivo += 1
            break
        elif trava_seguranca == 'nao' or trava_seguranca == 'não':
            ponto_negativo += 1
            break
        else:
            print('------------------')
            print('Opção Inválida!')
            print('------------------')
    while True:
        print('\n== Dispositivos Eletrônicos de Rastreamento ==')
        dispositivo_rastreamento = input('Você tem: Sim, Não --> \n').lower()
        if dispositivo_rastreamento == 'sim':
            ponto_positivo += 1
            break
        elif dispositivo_rastreamento == 'nao'or dispositivo_rastreamento == 'não':
            break
        else:
            print('------------------')
            print('Opção Inválida!')
            print('------------------')
    while True:
        print('\n== Cadeados Integrados == ')
        cadeados_bike = input('Você tem: Sim, Não --> \n').lower()
        if cadeados_bike == 'sim':
            ponto_positivo += 1
            break
        elif cadeados_bike == 'nao' or cadeados_bike == 'não':
            break
        else:
            print('------------------')
            print('Opção Inválida!')
            print('------------------')
    while True:
        print('\n== Sistemas de Alarme ==')
        sistema_alarme = input('Você tem: Sim, Não --> \n').lower()
        if cadeados_bike == 'sim':
            ponto_positivo += 2
            break
        elif cadeados_bike == 'nao' or cadeados_bike == 'não':
            break
        else:
            print('------------------')
            print('Opção Inválida!')
            print('------------------')
    while True:
        print('\n== Lugar de Armazenamento ==')
        lugar_armazenamento = input('Em qual lugar a sua Bike é guardada: Quintal, Garagem, Dentro de Casa, Rua --> \n').lower()
        if lugar_armazenamento == 'garagem' or lugar_armazenamento == 'dentro de casa' or lugar_armazenamento == 'casa':
            ponto_positivo += 1
            break
        elif lugar_armazenamento == 'quintal' or lugar_armazenamento == 'rua':
            ponto_negativo += 2
            break
        else:
            print('------------------')
            print('Opção Inválida!')
            print('------------------')
        print('='*50)  
        seguranca = [
            {'|Trava de seguranca|': trava_seguranca, '|Dispositivo de rastreamento|': dispositivo_rastreamento}
        ]
        seguranca = pd.DataFrame(seguranca)
        print(seguranca)
        seguranca2 = [
        {'|Cadeado|': cadeados_bike, '|Alarme|': sistema_alarme, '|Local de armazenamento|': lugar_armazenamento}
        ]
        seguranca2 = pd.DataFrame(seguranca2)
        print(seguranca2)
        print('='*50)
    # Variavel que será utilizada para sair do loop
        confirmacao = int(input('Confirma as informações? [1] SIM, [2] NÃO\n'))
        if confirmacao == 1:
            print('\nDados registrados com sucesso!\n')
        elif confirmacao == 2:
            print('\nOs dados foram cancelados.\n')
            recursos_de_seguranca_bike()
    recursos_de_seguranca = {
        'Trava de Segurança': trava_seguranca,
        'Dispositivo de Rastreamento': dispositivo_rastreamento,
        'Cadeados Integrados': cadeados_bike,
        'Sistema de Alarme': sistema_alarme,
        'Lugar de Armazenamento': lugar_armazenamento
    }
    print('--------------------------------')
    # As variáveis <ponto_positivos> e <ponto_negativos> serão usadas para validar a vistoria na função <menu()>
    return ponto_positivo, ponto_negativo, recursos_de_seguranca

# Função que recebe e armazena o acessorios da bike
def acessorios_bike():
    while True:
        quantidade = int(input('Quantos acessorios possui a sua Bike: '))
        if quantidade <= 0:
            print('Opção invalida!')
        else:
            break
    valores = 0
    lista_acessorios = []
    for i in range(quantidade):
        while True:
            acessorio = input(f'{i+1}.Nome:')
            if acessorio == '':
                print('Não pode ser vazio: ')
            else:
                break
        while True:
            valor = float(input(f'Valor: R$'))
            valores += valor
            if valor < 0:
                print('Não pode ser valor negativo!')
            else:
                break
        dicionario = {acessorio:valor}
        lista_acessorios.append(dicionario)
    print('Seus acessorios: ')
    for i in lista_acessorios:
        print(f'{i}')
    print(f'Valor Total dos acessorios: R${valores}')
    ponto_positivo = 0
    if valores >= 2000:
        ponto_positivo = 2
    print('='*50)
    tabela_acessorios = [
        {'|Total de acessorios|': quantidade}
    ]
    tabela_acessorios = pd.DataFrame(tabela_acessorios)
    print(tabela_acessorios)
    lista_de_acessorio = [
        {'|Nome e preco do acessorio|': lista_acessorios}
    ]
    lista_de_acessorio = pd.DataFrame(lista_de_acessorio)
    print(lista_de_acessorio)
    print('='*50)
    # Variavel que será utilizada para sair do loop
    confirmacao = int(input('Confirma as informações? [1] SIM, [2] NÃO\n'))   
    if confirmacao == 1:
        print('\nDados registrados com sucesso!\n')
    elif confirmacao == 2:
        print('\nOs dados foram cancelados.\n')
        criar_registro_bike()
    # As variáveis <ponto_positivos> e <ponto_negativos> serão usadas para validar a vistoria na função <menu()>
    return ponto_positivo, lista_acessorios
#Funcao que armazena o GitHub do DEVS
def github_devs():
    username= input('Qual o username que deseja encontrar?')
    url = f'https://api.github.com/users/{username}'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(data)
        print(f'Nome completo: {data["name"]}')
        print(f'Bio: {data["bio"]}')
        print(f'Localizacao: {data["location"]}')
        print(f'Seguidores: {data["followers"]}')
        print(f'Seguindo: {data["following"]}')
    else:
        print('Usuario nao encontrado!')
    # Variavael para sair do loop
    confirmando = int(input('Deseja conhecer o GitHub de mais algum DEV? [1] SIM, [2] NÃO\n'))   
    if confirmando == 1:
        print('\n Obrigado por utilizar nosso programa\n') 
    elif confirmando == 2:
        print('\n Volte sempre!\n')
        exibir_menu()        
# Função que faz a validação da vistoria com a utilizaçao de dois paramentros
def aceitacao_de_seguro(ponto_positivo, ponto_negativo):
    if ponto_positivo >= ponto_negativo :
        print('-*'*40)
        print('Parabens!!! Você pode fazer o contrato de seguro para a sua Bike!!!')
        print('-*' * 40)
    else:
        print('-*' * 40)
        print('Desculpe, você não possui pontos positivos suficientes para fazer o contrato de seguro.')
        print('-*' * 40)

# Funçao chave que engloba todas as funções do programa
def menu():
    encerrar_programa = True
    bike_registro = None
    dados_usuario = []
    ponto_negativo = 0
    ponto_positivo = 0

    while encerrar_programa:
        sair = False
        escolha = exibir_menu()

        while not sair:
            if escolha == '2':
                dados_user, idade = dados_pessoais()
                dados_usuario.append(dados_user)
                if idade > 2004:
                    print('-'*30)
                    print('Você não tem idade suficiente para adquirir o seguro da Porto!')
                    print('-' * 30)
                    sair = 1
                else:
                    contato = dados_de_contato()
                    dados_usuario.append(contato)
                    endereço = captura_dados_endereço()
                    dados_usuario.append(endereço)
                    sair = True  # Alterado para sair = True
            elif escolha == '1':
                bike_registro = criar_registro_bike()
                a, b, dicionario_componentes = capturar_componentes_bike()
                ponto_positivo += a
                ponto_negativo += b
                m, n, dicionario_recursos_segurança = recursos_de_seguranca_bike()
                ponto_positivo += m  # Corrigido para usar m
                ponto_negativo += n  # Corrigido para usar n
                acessorios = int(input('Você possui acessórios: [1] sim - [2] não: '))
                if acessorios == 1 or acessorios == 'sim':
                    z, lista_acessorios = acessorios_bike()
                    ponto_positivo += z
                else:
                    z = 0
                    lista_acessorios = []
                    print('Ok...')
                print(f'--'*20)
                print(f'Pontuação: \n{ponto_positivo}: Pontos Positivos\n{ponto_negativo}: Pontos Negativos')
                aceitacao_de_seguro(ponto_positivo, ponto_negativo)
                sair = True  # Alterado para sair = True
            elif escolha == '3':
                exibir_informacoes()
            elif escolha == '4':
                sair = True
            elif escolha == '5':
                github_devs()
            else:
                print('Opcao invalida!')
                
        print('-'*30)
        encerrar = int(input(' [1] - Voltar ao menu \n [2] - Sair do Programa \n -->'))
        if encerrar == 1:
            encerrar_programa = True
        else:
            encerrar_programa = False

    return bike_registro, dados_usuario, dicionario_componentes, dicionario_recursos_segurança, lista_acessorios

# Variáveis armazenam os valores retornados da função menu
bike_registro, dados_usuario, dicionario_componentes, dicionario_recursos_segurança, lista_acessorios = menu()

# Opção de visualizar as listas e/ou dicionários
print('== Opção de desenvolvedor ==')
opcao_extra = int(input('Exibir... '))
if opcao_extra == 1:
    print('Bike Registro:', bike_registro)
    print('Dados do Usuário:', dados_usuario)
    print('Componentes da Bike:', dicionario_componentes)
    print('Recursos de Segurança:', dicionario_recursos_segurança)
    print('Acessórios:', lista_acessorios)
else:
    print('Programa encerrado...')
