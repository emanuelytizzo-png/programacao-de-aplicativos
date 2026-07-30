import sqlite3 
 
def buscar_dados_dinamicos(nome_tabela, id_registro): 
    conexao = sqlite3.connect('sistema_escola.db') 
	cursor = conexao.cursor() 
     
	# O SQLite joga um erro de sintaxe operacional indicando que não aceita o caractere '?'. 
	# Não podemos parametrizar nomes de tabelas? Como resolver mantendo a segurança? 
    cursor.execute("SELECT * FROM ? WHERE id = ?", (nome_tabela, id_registro)) 
     
	print(cursor.fetchone()) 
    conexao.close() 
 
# R= O erro acontece porque o caractere ? só pode ser usado para parametrizar valores, e não nomes de tabelas ou colunas. 
# Por isso, o SQLite gera um erro de sintaxe ao tentar usar ? no lugar do nome da tabela.
# Para manter a segurança, é preciso verificar se o nome da tabela faz parte de uma lista de tabelas permitidas. 
# Depois dessa validação, o nome da tabela pode ser inserido na consulta, enquanto o id continua sendo passado como parâmetro.

correção do código:

import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro): 
    tabelas_permitidas = ["alunos", "professores", "turmas"]

if nome_tabela not in tabelas_permitidas: 
    print("Tabela inválida!") 
return

conexao = sqlite3.connect("sistema_escola.db") 
cursor = conexao.cursor()
