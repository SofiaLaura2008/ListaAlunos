from flask import Flask, render_template, request, redirect, abort
from models import db, AlunoModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alunos.bd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/Alunos')
def lista():
    alunos = AlunoModel.query.all()
    return render_template('lista.html',alunos = alunos)

@app.route('/Alunos/criar' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('pagina.html')

    if request.method == 'POST':
        alunoId = request.form['alunoId']
        nome = request.form['nome']
        idade = request.form['idade']
        serie = request.form['serie']
        aluno = AlunoModel(alunoId = alunoId, nome = nome, idade = idade, serie = serie)

        db.session.add(aluno)
        db.session.commit()
        return redirect('/Alunos')

@app.route('/Alunos/<int:id>')
def listaAlunos(id):
    aluno = AlunoModel.query.filter_by(alunoId=id).first()
    if aluno:
        return render_template('alunos.html', aluno=aluno)
    return f"Aluno com o id = {id} não existe"


@app.route('/Alunos/<int:id>/atualizar', methods=['GET', 'POST'])
def atualizar(id):
    aluno = AlunoModel.query.filter_by(alunoId=id).first()
    if not aluno:
        return f"Aluno com o id = {id} não existe"

    if request.method == 'POST':
        db.session.delete(aluno)
        db.session.commit()

        nome = request.form['nome']
        idade = request.form['idade']
        serie = request.form['serie']

        novo_aluno = AlunoModel(alunoId=id, nome=nome, idade=idade, serie=serie)
        db.session.add(novo_aluno)
        db.session.commit()
        return redirect(f'/Alunos/{id}')
    
    return render_template('atualizar.html', aluno=aluno)

        
@app.route('/Alunos/<int:id>/excluir', methods=['GET', 'POST'])
def excluir(id):
    aluno = AlunoModel.query.filter_by(alunoId=id).first()
    if not aluno:
        abort(404)  
    
    if request.method == 'POST':
        db.session.delete(aluno)
        db.session.commit()
        return redirect('/Alunos')

    return render_template('excluir.html', aluno=aluno)


if __name__ == "__main__":
    app.run(host="localhost", port=5000)