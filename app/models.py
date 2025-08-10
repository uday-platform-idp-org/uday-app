from flask_sqlalchemy import SQLAlchemy

postgres = SQLAlchemy()

class Empresa(postgres.Model):
    __tablename__ = 'empresas'  # Define explicitamente o nome da tabela
    id = postgres.Column(postgres.Integer, primary_key=True)
    cnpj = postgres.Column(postgres.String(18), nullable=False)
    nome = postgres.Column(postgres.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'cnpj': self.cnpj,
            'nome': self.nome
        }

def adicionar_empresa(cnpj, nome):
    nova = Empresa(cnpj=cnpj, nome=nome)
    postgres.session.add(nova)
    postgres.session.commit()
    return nova

def listar_empresas():
    return Empresa.query.all()