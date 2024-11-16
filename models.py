from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AlunoModel(db.Model):
    __tablename__ = "Aluno"
    id = db.Column (db.Integer, primary_key = True)
    alunoId = db.Column (db.Integer(), unique = True)
    nome = db.Column (db.String())
    idade = db.Column (db.Integer())
    serie = db.Column (db.String(80))

def __init__ (self, alunoId, nome, idade, serie):
    self.alunoId = alunoId
    self.nome = nome
    self.idade = idade
    self.serie = serie

def __repr__ (self):
    return f"{self.name}: {self.alunoId}"