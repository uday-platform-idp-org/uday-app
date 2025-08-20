from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models import adicionar_empresa, listar_empresas
import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    empresas = listar_empresas()
    return render_template('index.html', empresas=empresas)

@bp.route('/api/empresas', methods=['GET', 'POST'])
def api_empresas():
    if request.method == 'POST':
        data = request.get_json()
        cnpj = data.get('cnpj')
        nome = data.get('nome')

        if not cnpj or not nome:
            return jsonify({'erro': 'CNPJ e nome são obrigatórios'}), 400

        nova_empresa = adicionar_empresa(cnpj, nome)
        return jsonify(nova_empresa.to_dict()), 201

    elif request.method == 'GET':
        empresas = listar_empresas()
        return jsonify([e.to_dict() for e in empresas])

@bp.route('/cadastrar', methods=['POST'])
def cadastrar_form():
    cnpj = request.form['cnpj']
    nome = request.form['nome']
    adicionar_empresa(cnpj, nome)
    return redirect(url_for('main.index'))

health_bp = Blueprint('health', __name__)

@health_bp.route('/healthz')
def health_check():
    return jsonify({
        "Status": "OK",
        "Version": "1.0.0",
        "Tempo": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), 
    }), 200