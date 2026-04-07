senha_correta = "python123"
senha = ""

while senha != senha_correta:
    senha = input("digite a senha: ")

    if senha != senha_correta:
        print("senha incorreta. ")
        