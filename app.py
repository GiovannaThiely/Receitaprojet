from flask import Flask,g, render_template, request, redirect
import sqlite3

def ligar_banco():
  banco=g._database = sqlite3.connect('Receita.db')
  return banco

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Home.html',Titulo= 'Gestão de Receitas')

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html',Titulo='Cadastro de Receitas')

@app.route('/criar',methods=['POST','GET'])
def criar():
    banco=ligar_banco()
    cursor=banco.cursor()
    nome=request.form['nome']
    categoria=request.form['categoria']
    tempop=request.form['tempop']
    tempoc=request.form['tempoc']
    dificuldade=request.form['dificuldade']
    dicas=request.form['dicas']
    ingrediente=request.form['ingredientes']
    valornutricional=request.form['valornutricional']
    cursor.execute('''
        INSERT INTO Receita
        (Nome,Categoria,TempodePreparo,Tempodecozimento,Dificuldade,Dicas,Ingredientes,ValorNutricional)
        VALUES (?,?,?,?,?,?,?,?);
        ''',
        (nome,categoria,tempop,tempoc,dificuldade,dicas,ingrediente,valornutricional)

    )
    banco.commit()
    return redirect('/receita')

@app.route('/receita')
def receita():
    banco=ligar_banco()
    cursor=banco.cursor()
    cursor.execute('SELECT * FROM Receita;')
    Receita=cursor.fetchall()
    return render_template('Receita.html',Titulo='Cadastro de Receitas',ListaReceitas=Receita)

@app.teardown_appcontext #funçao para fechar o banco
def fechar_banco(exception):
    banco=ligar_banco()
    banco.close()

if __name__ == '__main__':
    app.run()
