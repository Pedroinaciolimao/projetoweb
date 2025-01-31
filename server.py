from flask import *
import dao
app = Flask(__name__)

app.secret_key = 'Khggj3h424j23hg44$#'

@app.route('/logout', methods=['POST', 'GET'])
def sair():
    session.pop('login')
    return render_template('index.html')

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
            session['login'] = login
            return render_template("bem_vindo.html")
        else:
            return render_template('login.html')
    return render_template('login.html')

@app.route('/')
def home():
    return render_template('bem_vindo.html')

@app.route('/exercicio')
def exercicio():
    return render_template('exercicio.html')

@app.route('/treino_peito')
def treino_peito():
    return render_template('treino_peito.html')

@app.route('/listausuarios')
def listausuarios():

    if 'login' in session:
        usuarios = dao.listausuarios()
        return render_template('Listausuarios.html', lista=usuarios)
    else:
        return render_template('index.html')

@app.route('/listar_exercicios')
def listar_exercicios():
    return render_template('listar_exercicios.html', treino=treino)
# Rota para adicionar um novo exercício

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        descricao = request.form['descricao']

        # Adiciona o exercício na lista
        treino.append({
            'nome': nome,
            'categoria': categoria,
            'descricao': descricao
        })
        return redirect(url_for('listar_exercicios'))

    return render_template('cadastrar.html')


# Rota para excluir um exercício do treino
@app.route('/excluir_exercicio', methods=['POST'])
def excluir_exercicio(exercicio):
    if 0 <= exercicio < len(treino):
        treino.pop(exercicio)
    return redirect(url_for('listar_exercicios'))


if __name__ == "__main__":
    app.run(debug=True)