from flask import Flask, render_template

app = Flask("__name__")

# Configurar o caminho para a pasta de templates
app.template_folder = 'src/templates'
app.static_folder = 'src/static'

@app.route("/") # criando rotas com decorator
def index():
    return render_template("index.html")

# @app.route("/dados.html")
# def contato():
#     return render_template("/dados.html")

@app.route("/quem_somos")
def quem_somos():
    return render_template("/quem_sonos/quem_somos.html")





