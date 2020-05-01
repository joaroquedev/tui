import sqlite3
import sys


connect = sqlite3.connect('tarefas.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
	name TEXT NOT NULL,
	content TEXT NOT NULL
);
''')

def menu():
	print("\t+"+"-"*30+"+\n")
	print("\t R : registrar tarefa")
	print("\t L : listar tarefas")
	print("\t S : sair\n")
	print("\t+"+"-"*30+"+")

def list():
	cursor.execute(f'''
		SELECT name, content FROM tarefas
	''')
	for tarefa in cursor.fetchall():
		ta = tarefa
		print(ta)

def insert(name,content):
	cursor.execute(f'''
		INSERT INTO tarefas (name, content)
		VALUES ('{name}', '{content}')
	''')

while True:
	menu()
	op = str(input("-$ ")).upper()
	if op not in ['R', 'L', 'A', 'S']:
		print("Opção inválida! ")
		continue

	elif op == 'R':
		print("Registrar tarefa.")
		nome = input("Qual o nome da tarefa: ")
		conteudo = input("Escreve sobre: ")
		insert(nome,conteudo)

	elif op == 'L':
		print("Listar todas tarfas")
		list()

	elif op == 'S':
		print("Encerrar...")
		break

connect.close()