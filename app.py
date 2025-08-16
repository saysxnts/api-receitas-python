# app.py
from flask import Flask, jsonify, request

# Cria a aplicação Flask
app = Flask(__name__)

# Nosso "banco de dados" em memória
receitas = [
    {
        "id": 1,
        "nome": "Pão com Ovo",
        "ingredientes": ["2 fatias de pão", "1 ovo", "sal"],
        "instrucoes": "Frite o ovo e coloque no pão."
    },
    {
        "id": 2,
        "nome": "Macarrão Alho e Óleo",
        "ingredientes": ["200g de macarrão", "3 dentes de alho", "azeite", "sal"],
        "instrucoes": "Cozinhe o macarrão e refogue o alho no azeite para misturar."
    }
]
next_id = 3

# --- NOSSOS ENDPOINTS (ROTAS) ---

# Rota para listar todas as receitas (GET /receitas)
@app.route('/receitas', methods=['GET'])
def get_receitas():
    return jsonify(receitas)

# Rota para buscar uma receita específica pelo ID (GET /receitas/<id>)
@app.route('/receitas/<int:id>', methods=['GET'])
def get_receita_por_id(id):
    for receita in receitas:
        if receita['id'] == id:
            return jsonify(receita)
    # Se o laço terminar e não encontrar, retorna erro 404
    return jsonify({"error": "Receita não encontrada"}), 404

# Rota para criar uma nova receita (POST /receitas)
@app.route('/receitas', methods=['POST'])
def create_receita():
    global next_id
    dados = request.get_json()

    # Validação simples
    if not dados or 'nome' not in dados or 'ingredientes' not in dados:
        return jsonify({"error": "Nome e ingredientes são obrigatórios"}), 400

    nova_receita = {
        "id": next_id,
        "nome": dados['nome'],
        "ingredientes": dados['ingredientes'],
        "instrucoes": dados.get('instrucoes', '') # .get() para um campo opcional
    }

    receitas.append(nova_receita)
    next_id += 1

    return jsonify(nova_receita), 201 # 201 Created

# Ponto de entrada para rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True) # debug=True faz o servidor reiniciar automaticamente a cada alteração