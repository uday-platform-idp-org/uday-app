import time
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from sqlalchemy import text  # <- IMPORTANTE
from models import postgres
from routes import bp
from dotenv import load_dotenv
from routes import bp, health_bp  # importe os blueprints

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(bp)         # rotas principais
app.register_blueprint(health_bp)  # healthcheck


postgres.init_app(app)

def wait_for_db():
    """Espera até que o banco esteja disponível."""
    max_retries = 10
    for attempt in range(max_retries):
        try:
            with app.app_context():
                postgres.session.execute(text("SELECT 1"))  # <- AQUI
            print("✅ Banco de dados conectado!")
            return True
        except OperationalError:
            print(f"⏳ Banco não disponível, tentando novamente... ({attempt+1}/{max_retries})")
            time.sleep(2)
    print("❌ Não foi possível conectar ao banco.")
    return False

if wait_for_db():
    with app.app_context():
        postgres.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')