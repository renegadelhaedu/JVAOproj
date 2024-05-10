from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == '123':
        return render_template('index.html', username=username)
    else:
        return render_template('login.html', error='Usuário ou senha inválidos!')


if __name__ == "__main__":
    app.run(debug=True)
