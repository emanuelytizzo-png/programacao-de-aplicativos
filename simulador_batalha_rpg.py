vida_personagem = 100
rodada = 1
def sofrer_dano(vida_atual, valor_dano):
    """Subtrai o dano da vida e retorna o novo valor."""
    nova_vida = vida_atual - valor_dano
    return nova_vida

print("--- Início da Batalha ---")
print(f"Vida Inicial: {vida_personagem}")

while vida_personagem > 0:
    print(f"\n--- Rodada {rodada} ---")
    
    try:
        dano = int(input("Quanto de dano o monstro causou? "))
        vida_personagem = sofrer_dano(vida_personagem, dano)
        if vida_personagem < 0:
            vida_personagem = 0
            
        print(f"Vida atual: {vida_personagem}")
        if vida_personagem <= 0:
            print("Game Over! Você foi derrotado.")
            break
            
        rodada += 1
        
    except ValueError:
        print("Por favor, digite um número válido.")

print("--- Fim do Jogo ---")