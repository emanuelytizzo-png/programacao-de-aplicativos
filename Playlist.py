playlist = ["Musica 1", "Musica 2", "Musica 3", "Musica 4", "Musica 5"]
print(f"Playlist original: {playlist}")
playlist.remove("Musica 3")
print(f"remover 'Musica 3': {playlist}")
primeira_musica = playlist.pop(0)
print(f"Música removida pelo índice: {primeira_musica}")
print(f"Playlist final: {playlist}")
print(f"Música na posição 1: {playlist[1]}")