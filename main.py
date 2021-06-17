
from classes import Registros, Usuario, Admnistrador, Cliente, Manga, Anime, X
from funcoes_aux import *

def MenuAdmin(Registro):
    opMenuAdmin = int(input("\n Você quer: \n Cadastrar novas obras -> 1 \n Cadastrar novo usuário -> 2 \n logout -> 3 \n"))
    screen_clear()

    if opMenuAdmin == 1:
        t = int(input("Quantas obras você quer colocar?  "))

        for x in range(0, t):
            nomeObra = input("Qual o nome da obra? \n")
            genObra = input("Qual é o genero da obra? \n")
            tipoObra = int(input("Qual é o tipo da obra? \n Manga =1 Anime = 2 \n"))
            quantCapitulos = float(input("Quantidade de Capitulos: " if tipoObra == 1 else "Quantidade de Episodios: "))
            if tipoObra == 1:
                nomeAutor = input("Qual é o autor? \n")
                nomeIlustrador = input("Qual é o ilustrador? \n")
                novoManga = Manga(nomeObra, genObra, quantCapitulos, nomeAutor, nomeIlustrador)
                novoManga.print_manga()

            if tipoObra == 2:
                nomeEstudio = input("Qual é o Estudio? \n")
                nomeSupervisor = input("Quem é o Supervisor? \n")
                novoAnime = Anime(nomeObra, genObra, quantCapitulos, nomeEstudio, nomeSupervisor)
                novoAnime.print_anime()

    if opMenuAdmin == 2:
        nomeAdmin = input("Qual o nome do novo Administrador? \n")
        emailAdmin = input("Qual o e-maildo novo Administrador? \n")
        cargoAdmin = input("Qual o cargo do novo Administrador? \n")
        novoNivelPrivilegio = input("Qual o nível de privivégio do novo Administrador? \n")
        senhaAdmin = input("Crie uma senha: ")
        confirmaSenha = input("Confirme a nova senha: ")

        if senhaAdmin == confirmaSenha:
            novoAdmin = Admnistrador(nomeAdmin, emailAdmin, senhaAdmin, cargoAdmin, novoNivelPrivilegio)
            Registro.add_novoAdmin(novoAdmin)
            MenuAcesso(Registro)
        else:
            print("Senhas diferentes!")
            MenuAdmin(Registro)

    if opMenuAdmin == 3:
        MenuAcesso(Registro)

    MenuAdmin(Registro)

def MenuCliente(Registro, Cliente):
    tempListManga = Manga.todosMangas
    tempListAnime = Anime.todosAnimes
    tempList = X.lista
    opMenuCliente = int(
        input("\n Você quer: \n Ver lista de Mangas? -> 1 \n Ver lista de Animes -> 2 \n Adicionar na lista de favoritos"
              " -> 3 \n Adicionar na lista de finalizados -> 4 \n Adicionar na lista de pretendidos -> 5 \n  Ver meus favoritos -> 6"
              "\n Ver finalizados -> 7 \n Ver pretendidos -> 8 \n Logout -> 9 \n"))

    screen_clear()

    if opMenuCliente == 1:
        print_mangaList(tempListManga)
        MenuCliente(Registro, Cliente)

    if opMenuCliente == 2:
        print_animeList(tempListAnime)
        MenuCliente(Registro, Cliente)

    if opMenuCliente == 3:
        print_lista(tempList)

        novoFavNum = int(input("\n Qual item voce deseja adiconar a sua lista de favoritos? \n"))
        Cliente.add_favorito(tempList[novoFavNum])
        MenuCliente(Registro, Cliente)

    if opMenuCliente == 4:
        print_lista(tempList)

        novoFinNum = int(input("\n Qual item voce deseja adiconar a sua lista de finalizados? \n"))
        Cliente.add_finalizados(tempList[novoFinNum])
        MenuCliente(Registro, Cliente)

    if opMenuCliente == 5:
        print_lista(tempList)

        novoPretendNum = int(input("\n Qual item voce deseja adiconar a sua lista de pretenditos? \n"))
        Cliente.add_pretendidos(tempList[novoPretendNum])
        MenuCliente(Registro, Cliente)

    if opMenuCliente == 6:
        print_lista(Cliente.get_favoritos())
        MenuCliente(Registro, Cliente)

    if opMenuCliente == 7:
        print_lista(Cliente.get_finalizados())
        MenuCliente(Registro, Cliente)

    if opMenuCliente == 8:
        print_lista(Cliente.get_pretendidos())
        MenuCliente(Registro, Cliente)

    if opMenuCliente == 9:
        MenuAcesso(Registro)

    else:
        MenuCliente(Registro, Cliente)

def MenuAcesso(Registro):
    tempListCliente = Registro.get_listaClientes()
    tempListAdmin = Registro.get_listaAdmins()
    acesso = int(input("\n Login ou Cadastro? \n Login = 1  Cadastro = 2  Finalizar = 3 \n"))
    screen_clear()
    if acesso == 1:
        nomeLogin = input("\n Qual seu nick de usuário? \n")

        for element in range(0, len(tempListCliente)):
            if tempListCliente[element].get_nomeUsuario() == nomeLogin:
                senhaLogin = input("\n Qual sua senha? \n")
                if tempListCliente[element].compara_senha(senhaLogin) == True:
                    print("Logado com Sucesso!")
                    MenuCliente(Registro, tempListCliente[element])
                else:
                    print("Senha Incorreta, tente novamente...")
                    MenuAcesso(Registro)

        for element in range(0, len(tempListAdmin)):
            if tempListAdmin[element].get_cargo() == nomeLogin:
                senhaLogin = input("\n Qual sua senha? \n")
                if tempListAdmin[element].compara_senha(senhaLogin) == True:
                    print("Logado com Sucesso!")
                    MenuAdmin(Registro)
                else:
                    print("Senha Incorreta, tente novamente...")
                    MenuAcesso(Registro)

        print("Usuário não encontrado!")
        MenuAcesso(Registro)

    if acesso == 2:
        nomeCliente = input("Qual o seu nome? \n")
        emailCliente = input("Qual o seu e-mail? \n")
        idadeCliente = input("Qual a sua idade? \n")
        nicknameCliente = input("Qual é o seu nick de usuário? \n")
        senhaCliente = input("Crie uma senha: ")
        confirmaSenha = input("Confirme sua senha: ")
        if senhaCliente == confirmaSenha:
            novoCliente = Cliente(nomeCliente, emailCliente, senhaCliente, idadeCliente, nicknameCliente)
            Registro.add_novoCliente(novoCliente)
            MenuAcesso(Registro)
        else:
            print("Senhas diferentes!")
            MenuAcesso(Registro)

    if acesso == 3:
        return None

if __name__ == '__main__':
    Registro = Registros()
    rootAdmin = Admnistrador("root", "root@root.com", "root1337", "root", 10)
    clientSeed1 = Cliente("Susannah", "susannah@gurgel.com", "123", "23", "su")
    mangaSeed1 = Manga("Naruto", "Ação", 500, "Nakano", "Zuco")
    animeSeed1 = Anime("One Piece", "Aventura", 900, "Natsumoto", "Naburo")
    Registro.add_novoCliente(clientSeed1)
    Registro.add_novoAdmin(rootAdmin)
    MenuAcesso(Registro)
