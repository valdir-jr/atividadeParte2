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