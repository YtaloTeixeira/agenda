AGENDA = {}

def mostraAgenda():
    if AGENDA:
        for contato in AGENDA:
            buscaContato(contato)
    else:
        print()
        print(" >>>> A agenda está vazia!!! <<<< ")
        print()


def buscaContato(contato):
    try:
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]["tel"])
        print("E-mail:", AGENDA[contato]["email"])
        print("Endereço:", AGENDA[contato]["endereco"])
        print("---------------")
    except KeyError:
        print()
        print(" >>>> O contato {} não foi encontrado na agenda !!! <<<< ".format(contato))
        print()

def lerDetalhes():
    tel = input("Digite o telefone do contato: ")
    email = input("Digite o e-mail do contato: ")
    endereco = input("Digite o endereço do contato: ")
    return tel, email, endereco

def adicionaEditaContato(contato, tel, email, endereco):
    AGENDA[contato] = {"tel": tel, "email": email, "endereco": endereco}

    salvaAgenda()

    print()
    print(
        ">>>> O contato {} foi adicionado/editado com sucesso!!! <<<<".format(contato)
    )
    print()


def excluiContato(contato):
    try:
        AGENDA.pop(contato)
        salvaAgenda()
        print()
        print(" >>>> O contato {} foi excluído com sucesso!!! <<<<".format(contato))
        print()
    except KeyError:
        print()
        print(" >>>> O contato {} não foi encontrado na agenda!!! <<<<".format(contato))
        print()


def exportaContatos(nomeArquivo):
    try:
        with open(nomeArquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['tel']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                
                arquivo.write("{},{}, {}, {}\n".format(contato, telefone, email, endereco))
        print(" >>>> Agenda exportada!!! <<<< ")
    except Exception as e:
        print(" >>>>Ocorreu um erro ao tentar exportar os contatos da agenda <<<<")
        print(e)


def importaContatos(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                adicionaEditaContato(nome, telefone, email, endereco)
    except FileNotFoundError as e:
        print("Arquivo não encontrado")
    except Exception as e:
        print(" >>>> Erro inesperado ao tentar importar os contatos <<<< ")
        print(e)


def salvaAgenda():
    exportaContatos('database.csv')


def carregarAgenda():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {"tel": telefone, "email": email, "endereco": endereco}
            print(" >>>> Database carregado com sucesso!!! <<<< ")
            print(" >>>> {} contatos carregados <<<<".format(len(AGENDA)))
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as e:
        print(" >>>> Erro inesperado ao tentar importar os contatos <<<< ")
        print(e)


def mostraMenu():
    print("----- AGENDA -----")
    print("1 - Mostrar todos os contatos da agenda")
    print("2 - Buscar contato")
    print("3 - Adicionar contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("6 - Exportar contatos .CSV")
    print("7 - Importar contatos")
    print("0 - Fechar agenda")
    print("------------------")

carregarAgenda()
while True:
    mostraMenu()

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        mostraAgenda()
    elif opcao == "2":
        contato = input("Digite o nome do contato: ")
        buscaContato(contato)
    elif opcao == "3":
        contato = input("Digite o nome do contato: ")

        try:
            AGENDA[contato]
            print(">>> O contato {} já está registrado na agenda!!! <<<".format(contato))
        except KeyError:
            tel, email, endereco = lerDetalhes()
            adicionaEditaContato(contato, tel, email, endereco)
    elif opcao == "4":
        contato = input("Digite o nome do contato: ")

        try:
            AGENDA[contato]
            tel, email, endereco = lerDetalhes()
            adicionaEditaContato(contato, tel, email, endereco)
        except KeyError:
            print(" >>>> Contato Inexiste!!!")
    elif opcao == "5":
        contato = input("Digite o nome do contato que quer exlcuir: ")
        excluiContato(contato)
    elif opcao == '6':
        nomeArquivo = input("Digite o nome do arquivo para exportar: ")
        exportaContatos(nomeArquivo)
    elif opcao == '7':
        nomeArquivo = input("Digite o nome do arquivo: ")
        importaContatos(nomeArquivo)
    elif opcao == "0":
        print("Fechando a agenda...")
        break
    else:
        print("Escolha um opção válida!")
