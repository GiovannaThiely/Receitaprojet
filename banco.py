import sqlite3
conexao=sqlite3.connect('Receita.db')
cursor=conexao.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS Receita(
           ID INTEGER PRIMARY KEY,
           Nome TEXT,
           Categoria TEXT,
           TempodePreparo TEXT,
           Tempodecozimento TEXT,
           Dificuldade TEXT,
           Dicas TEXT,
           Ingredientes TEXT,
           ValorNutricional TEXT)
''')
conexao.close()

