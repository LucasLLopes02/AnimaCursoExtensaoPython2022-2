# Primeiro passo: Importar a biblioteca sqlite3
import sqlite3

#Segundo passo: Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#Terceiro passo: Criar um objeto do tipo cursor
cursor = conexao.cursor()

#Quarto passo: Comando para inserir no banco de dados
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

#Quinto passo: Executar o comando SQL
cursor.execute(sql)

#Sexto passo: Confirmar o INSERT com commit() e fechar o banco
conexao.commit()
conexao.close()
