# N1 - PARTE 2
# GRUPO 5

def desenharMenu():
    print("0 - Sair")
    print("1 - Cadastrar um usuário")
    print("2 - Exibir todos os usuários (ordem de cadastro)")
    print("3 - Exibir todos os usuários (ordem de alfabética)")
    print("4 - Verificar usuário (nome)")
    print("5 - Remover usuário")
    print("6 - Alterar nome usuário")

def criarUsuario():
    novoUsuario = {}
    novoUsuario["nome"] = input("Coloque o nome completo do usuário: ")
    novoUsuario["email"] = input("Coloque o e-mail: ")
    return novoUsuario

def exibirPorOrdemCadastro(listaUsuarios : list):
    for umUsuario in listaUsuarios:
        print(umUsuario)        

def exibirPorOrdemAlfabetica(listaUsuarios : list):
    ordemAlfabetica = sorted(listaUsuarios, key=lambda obj: obj["nome"])
    for umUsuario in ordemAlfabetica:
        print(umUsuario)
        
def verificarPorNome(nome, listaUsuarios):
    for usuario in listaUsuarios:
        if (usuario["nome"] == nome):
            return usuario

def removerPorEmail(email, listaUsuarios):
    for usuario in listaUsuarios:
        if (usuario["email"] == email):
            return usuario     

def alterarPorEmail(email, listaUsuarios):
    nomeNovo = str(input("Qual será o novo nome do usuário? "))
    for usuario in listaUsuarios:
        if (usuario["email"] == email):
            usuario['nome'] = nomeNovo
            return usuario   
def main():
    listaUsuarios = []

    desenharMenu()
    opcao = int(input("\nDigite qual a opcao desejada: "))

    while(opcao != 0):
        if(opcao == 1):
            print("\n[OPTION]Cadastrar um novo usuário")
            listaUsuarios.append(criarUsuario())
            print("\n[SUCESS]Usuário Cadastrado")
            opcao = int(input("\nDigite qual a opcao desejada: "))

        elif(opcao == 2):
            print("\n[OPTION]Exibir por ordem de Cadastro")
            exibirPorOrdemCadastro(listaUsuarios)
            opcao = int(input("\nDigite qual a opcao desejada: "))

        elif(opcao == 3):
            print("\n[OPTION]Exibir por ordem alfabética")
            exibirPorOrdemAlfabetica(listaUsuarios)
            opcao = int(input("\nDigite qual a opcao desejada: "))

        elif(opcao == 4):
            print("\n[OPTION]Buscar usuário (nome)")
            nome = str(input("Qual nome quer buscar? "))
            print(verificarPorNome(nome,listaUsuarios))
            opcao = int(input("\nDigite qual a opcao desejada: "))

        elif(opcao == 5):
            print("\n[OPTION]Remover usuário (e-mail)")
            email = input("Qual o e-mail do usuário que quer remover? ")
            listaUsuarios.remove(removerPorEmail(email, listaUsuarios))
            print("\n[SUCESS]Usuário removido")
            opcao = int(input("\nDigite qual a opcao desejada: "))

        elif(opcao == 6):
            print("\n[OPTION]Alterar usuário (e-mail)")
            email = str(input("Qual é o email do usuário? "))
            alterarPorEmail(email, listaUsuarios)
            print("\n[SUCESS]Usuário alterado")
            opcao = int(input("\nDigite qual a opcao desejada: "))


if __name__ == "__main__" :
    main()