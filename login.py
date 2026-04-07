senha_correta = "1234"

tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha_usuario = input("Digite a senha: ")
    if senha_usuario == senha_correta:
        print("Acesso permitido!")
        break  # Sai do loop se a senha estiver correta
    else:
        tentativas += 1
        print(f"Senha incorreta! Tentativa {tentativas} de {max_tentativas}.")
if tentativas == max_tentativas:
    print("Acesso bloqueado.") 