from flask import Flask, render_template, request

app = Flask("__name__")

# Configuração do Jinja
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Configurar o caminho para a pasta de templates
app.template_folder = 'src/templates'

# Configurar o caminho para a pasta de arquivos estáticos
app.static_folder = 'src/static'

botao = ''

@app.route("/") # criando rotas com decorator
def index():
    return render_template("index.html")

@app.route("/dados.html", methods=['GET', 'POST'])
def dados():
    global botao
    if request.method == 'POST':
        botao = request.form.get('botao')
    return render_template("/dados/dados.html", resultado=botao)

# @app.route("/conheca.html")
# def quem_somos():
#     return render_template("conheca.html")





