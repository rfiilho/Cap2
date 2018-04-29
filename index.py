from datetime import *

### Cadastro de Usuário
def cadastrarUsuario(lista):
    atual = datetime.now()
    data = atual.date()
    hora = atual.time()
    x = "S"
    while x == "S":
        usuario = [input("Nome Completo: "), input("Apelido: "), input("Cargo: "), input("Nível de Acesso: "), data, hora]
        lista.append(usuario)
        print("Usuário cadastrado com sucesso!")
        x = input("Digite S para continuar: ").upper()
    menu()

### Pesquisa de Usuário
def pesquisaUsuario(lista):
    x = "S"
    while x == "S":
        busca = input("Digite o apelido do usuário: ")
        for elemento in lista:
            if busca == elemento[1]:
                print("Nome Completo........: ", elemento[0])
                print("Cargo................: ", elemento[2])
                print("Nível................: ", elemento[3])
            else:
                print("Nenhum usuário cadastrado com esse apelido")
        x = input("Digite S para continuar: ").upper()
    menu()

### Listamento de Super-Usuários
def listarSU(lista):
    tipo = "SU"
    for elemento in lista:
        if tipo == elemento[3]:
            print("Nome Completo........: ", elemento[0])
            print("Apelido..............: ", elemento[1])
            print("Cargo................: ", elemento[2])
            print("\n")
    menu()

### Exclusão de Usuário
def excluirUsuario(lista):
    x = "S"
    while x == "S":
        busca = input("Digite o apelido do usuário que deseja excluir: ")
        for elemento in lista:
            if busca == elemento[1]:
                lista.remove(elemento)
                print("Usuário excluído com sucesso!")
        x = input("Digite S para continuar: ").upper()
    menu()

### Listamento de Usuários
def listarUsuarios(lista):
    for elemento in lista:
        print("Nome Completo.........: ", elemento[0])
        print("Apelido...............: ", elemento[1])
        print("Cargo.................: ", elemento[2])
        print("Nível.................: ", elemento[3])
        print("\n")
    menu()

### Exibir Log de Usuários
def exibirLog(lista):
    print("\n")
    for elemento in lista:
        print("Usuário: ", elemento[0], " | Timestamp: ", elemento[4], " ", elemento[5])
    menu()

###  Exibir Menu
def menu():
    print("O que você deseja fazer?")

    print("\n1- Cadastrar um usuário")
    print("2- Pesquisar um usuário")
    print("3- Listar todos os super-usuários")
    print("4- Excluir um usuário")
    print("5- Listar todos os usuários")
    print("6- Exibir log do sistema")

    resposta = input("\nEscolha um número: ")

    if resposta == "1":
        print("Cadastrando Usuário")
        cadastrarUsuario(db)
    elif resposta == "2":
        print("Pesquisando usuário")
        pesquisaUsuario(db)
    elif resposta == "3":
        print("Listando todos os super-usuários")
        listarSU(db)
    elif resposta == "4":
        print("Excluindo um usuário")
        excluirUsuario(db)
    elif resposta == "5":
        print("Listando todos os usuários")
        listarUsuarios(db)
    elif resposta == "6":
        print ("Exibindo o log do sistema")
        exibirLog(db)
    else:
        menu()


db = []
menu()