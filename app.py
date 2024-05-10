from flask import Flask, render_template, request
import dao

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('usuario')
    password = request.form.get('senha')

    if username == 'admin' and password == '123':
        return render_template('index.html', username=username)
    else:
        return render_template('login.html', error='Usuário ou senha inválidos!')

@app.route('/pagecadastrarusuario')
def pagecadastrouser():
    return render_template('cadastrousuario.html')

@app.route('/cadastrarnovousuario', methods=['POST'])
def cadastrar_usuario():

    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    tipo = request.form.get('tipo')

    if(dao.inserir_usuario(nome, email, senha, tipo)):
        return render_template('login.html')
    else:
        msg = 'Erro: usuario já cadastrado'
        return render_template('login.html', error=msg)


if __name__ == "__main__":
    app.run(debug=True)
