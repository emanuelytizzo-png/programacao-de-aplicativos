def contar_caracteres(texto):
    return len(texto)

nome_usuario = input("Digite um nome de usuário: ")

tamanho = contar_caracteres(nome_usuario)

if tamanho < 5:
    print("Nome de usuário muito curto")
else:
    print("Nome aceito")