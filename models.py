from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Empresa(db.Model):
    __tablename__ = 'empresas'  # Define explicitamente o nome da tabela
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(18), nullable=False)
    nome = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'cnpj': self.cnpj,
            'nome': self.nome
        }

def adicionar_empresa(cnpj, nome):
    nova = Empresa(cnpj=cnpj, nome=nome)
    db.session.add(nova)
    db.session.commit()
    return nova

def listar_empresas():
    return Empresa.query.all()