from abc import ABC, abstractmethod

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

    def print_lista(self):
        for element in range(0, len(self.lista)):
            print(str(element) + " -> " + self.lista[element].get_nome() + " - " + "Manga" if type(self.lista[element]) == Manga
                else str(element) + " -> " + self.lista[element].get_nome() + " - " + "Anime")

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

    def print_manga(self, manga = None):
        if manga == None:
            manga = self
        print(f'Nome: {manga.get_nome()}')
        print(f'Genero: {manga.get_genero()}')
        print(f'Capitulos: {manga.get_capitulo_episodio()}')
        print(f'Volumes: {manga.temporada_volume()}')
        print(f'autor: {manga.get_autor()}')
        print(f'Ilustrador:{manga.get_ilustrador()}')

    def print_mangaList(self):
        for element in range(0, self.todosMangas):
            self.print_manga(self.todosMangas[element])

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

    def print_anime(self, anime = None):
        if anime == None:
            anime = self
        print(f'Nome: {anime.get_nome()}')
        print(f'Genero: {anime.get_genero()}')
        print(f'Capitulos: {anime.get_capitulo_episodio()}')
        print(f'Volumes: {anime.temporada_volume()}')
        print(f'Estudio: {anime.get_estudio()}')
        print(f'Supervisor: {anime.get_supervisor()}')
    
    def print_animeList(self):
        for element in range(0, self.todosAnimes):
            self.print_anime(self.todosAnimes[element])

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
