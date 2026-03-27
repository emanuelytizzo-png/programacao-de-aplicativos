senha_correta = "1234"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")
    
    if senha != senha_correta:
        print("Senha incorreta. ")

print("Bem-vindo")