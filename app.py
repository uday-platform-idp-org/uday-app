from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Empresa
from routes import bp
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuração do banco
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco
db.init_app(app)

# Cria tabelas
with app.app_context():
    db.create_all()

# Registra rotas
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')