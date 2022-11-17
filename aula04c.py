# Primeiro passo: Importar a biblioteca sqlite3
import sqlite3

#Passos 2 e 3 virarão função conectar()
def conectar():
  
  #Segundo passo: Estabelecer conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")

  #Terceiro passo: Criar um objeto do tipo cursor
  cursor = conexao.cursor()

  return conexao, cursor


