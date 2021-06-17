from abc import ABC, abstractmethod
import os

def print_manga(novoManga):
    print(f'Nome: {novoManga.get_nome()}')
    print(f'Genero: {novoManga.get_genero()}')
    print(f'Capitulos: {novoManga.get_capitulo_episodio()}')
    print(f'Volumes: {novoManga.temporada_volume()}')
    print(f'autor: {novoManga.get_autor()}')
    print(f'Ilustrador:{novoManga.get_ilustrador()}')

def print_anime(novoAnime):
    print(f'Nome: {novoAnime.get_nome()}')
    print(f'Genero: {novoAnime.get_genero()}')
    print(f'Capitulos: {novoAnime.get_capitulo_episodio()}')
    print(f'Volumes: {novoAnime.temporada_volume()}')
    print(f'Estudio: {novoAnime.get_estudio()}')
    print(f'Supervisor: {novoAnime.get_supervisor()}')

def print_animeList(listaAnimes):
    for element in range(0, len(listaAnimes)):
        print_anime(listaAnimes[element])

def print_mangaList(listaMangas):
    for element in range(0, len(listaMangas)):
        print_manga(listaMangas[element])

def print_lista(lista):
    for element in range(0, len(lista)):
        print(str(element) + " -> " + lista[element].get_nome() + " - " + "Manga" if type(lista[element]) == Manga
              else str(element) + " -> " + lista[element].get_nome() + " - " + "Anime")

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

class X(ABC):
    genero = None
    nome = None
    capitulo_episodio = None
    lista = []

    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_capitulo_episodio(self):
        return self.capitulo_episodio

    def get_lista(self):
        return X.lista

    @abstractmethod
    def temporada_volume(self):
        pass

class Manga(X):
    todosMangas = []

    def __init__(self, nome, genero, capitulo_episodio, autor, ilustrador):
        self.genero = genero
        self.nome = nome
        self.capitulo_episodio = capitulo_episodio
        self.autor = autor
        self.ilustrador = ilustrador
        Manga.todosMangas.append(self)
        X.lista.append(self)

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def get_ilustrador(self):
        return self.ilustrador

    def temporada_volume(self):
        temp = self.get_capitulo_episodio()
        return temp / 8

class Anime(X):
    todosAnimes = []

    def __init__(self, nome, genero, capitulo_episodio, estudio, supervisor):
        self.genero = genero
        self.nome = nome
        self.capitulo_episodio = capitulo_episodio
        self.estudio = estudio
        self.supervisor = supervisor
        Anime.todosAnimes.append(self)
        X.lista.append(self)

    def get_estudio(self):
        return self.estudio

    def get_supervisor(self):
        return self.supervisor

    def temporada_volume(self):
        temp = self.get_capitulo_episodio()
        return temp / 12

class Usuario(ABC):
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_senha(self):
        return self.senha

    def set_senha(self, senha):
        self.senha = senha

class Admnistrador(Usuario):
    def __init__(self, nome, email, senha, cargo, nivelPrivilegio):
        super().__init__(nome, email, senha)
        self.cargo = cargo
        self.nivelPrivilegio = nivelPrivilegio

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_nivelPrivilegio(self):
        return self.nivelPrivilegio

    def set_nivelPrivilegio(self, nivelPrivilegio):
        self.nivelPrivilegio = nivelPrivilegio

    def compara_senha(self, senhaDigitada):
        if senhaDigitada == self.senha:
            return True
        else:
            return False

class Cliente(Usuario):
    def __init__(self, nome, email, senha, idade, nomeUsuario):
        super().__init__(nome, email, senha)
        self.idade = idade
        self.nomeUsuario = nomeUsuario
        self.favoritos = []
        self.finalizados = []
        self.pretendidos = []

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

    def get_nomeUsuario(self):
        return self.nomeUsuario

    def set_nomeUsuario(self, nomeUsuario):
        self.nomeUsuario = nomeUsuario

    def compara_senha(self, senhaDigitada):
        if senhaDigitada == self.senha:
            return True
        else:
            return False

    def add_favorito(self, favorito):
        self.favoritos.append(favorito)

    def add_finalizados(self, finalizados):
        self.finalizados.append(finalizados)

    def add_pretendidos(self, pretendidos):
        self.pretendidos.append(pretendidos)

    def get_favoritos(self):
        return self.favoritos

    def get_finalizados(self):
        return self.finalizados

    def get_pretendidos(self):
        return self.pretendidos

class Registros():
    listaClientes = []
    listaAdmins = []

    def get_listaClientes(self):
        return Registros.listaClientes

    def add_novoCliente(self, novoCliente):
        Registros.listaClientes.append(novoCliente)

    def get_listaAdmins(self):
        return Registros.listaAdmins

    def add_novoAdmin(self, novoAdmin):
        Registros.listaAdmins.append(novoAdmin)

def MenuAdmin(Registro):
    lista = []
    listaAnimes = []
    listaMangas = []

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
                print_manga(novoManga)
                lista.append(novoManga)
            if tipoObra == 2:
                nomeEstudio = input("Qual é o Estudio? \n")
                nomeSupervisor = input("Quem é o Supervisor? \n")
                novoAnime = Anime(nomeObra, genObra, quantCapitulos, nomeEstudio, nomeSupervisor)
                print_anime(novoAnime)
                lista.append(novoAnime)

        for y in range(0, len(lista)):
            if type(lista[y]) == Anime:
                listaAnimes.append(lista[y])
            if type(lista[y]) == Manga:
                listaMangas.append(lista[y])

        print_animeList(listaAnimes)
        print_mangaList(listaMangas)

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
    else:
        print("Opção não encontrada! \n Tente novamente :) ")
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
