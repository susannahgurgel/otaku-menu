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
