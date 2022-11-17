# Primeiro passo: Importar a biblioteca sqlite3
import sqlite3

#Segundo passo: Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#Terceiro passo: Criar um objeto do tipo cursor
cursor = conexao.cursor()

#Quarto passo: Comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#Quinto passo: Executar o comando SQL no SQlite (no cursor)
cursor.execute(sql)

#Sexto passo: Exibir a consulta com todos os nomes de heróis e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")