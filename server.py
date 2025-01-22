from flask import Flask, render_template, request, redirect, url_for
import dao
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        login = request.form.get("login")
        senha = request.form.get("senha")

        if dao.inserir_user(login, senha, nome):
            msg= 'Cadastro feito com sucesso'
            return render_template('login.html', texto=msg)
        else:
            msg= 'Cadastro não realizado'
            return render_template("index.html", texto=msg)

    else:
        return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form.get("login")
        senha = request.form.get("senha")

        if len(dao.login(login, senha)) > 0:
            return render_template("bem_vindo.html")
        else:
            return render_template('login.html')
    return render_template('login.html')

@app.route('/')
def home():
    return render_template('bem_vindo.html')

@app.route('/treino_peito')
def treino_peito():
    return render_template('treino_peito.html')

@app.route('/listausuarios')
def listausuarios():
    usuarios = dao.listausuarios()
    print(usuarios)
    return render_template('Listausuarios.html', lista=usuarios)

if __name__ == "__main__":
    app.run(debug=True)