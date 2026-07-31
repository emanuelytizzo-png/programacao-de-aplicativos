import sqlite3

def buscar_professsor(id_prof):
    conexao = sqlite3
    cursor = conexao.cursor()

# O python reclama de "Incorrect number of bindings".
# Estamos passando a variável, por que ocorre o erro?

cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof))
resultado = cursor.fetchone()
print(resultado)
conexao.close()

#R= O erro acontece porque (id_prof) não é uma tupla, e sim apenas a variável entre parênteses. 
# O método execute() espera que os parâmetros sejam passados em uma sequência (como uma tupla ou lista).

correção dos código:

import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT nome FROM professores WHERE id = ?",
        (id_prof,)
    )

    resultado = cursor.fetchone()
    print(resultado)

    conexao.close()
