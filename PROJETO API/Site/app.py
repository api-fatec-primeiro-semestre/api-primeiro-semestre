from flask import Flask, render_template, url_for

app = Flask("__name__")

@app.route("/") # criando rotas com decorator
def index():
    return render_template("index.html")

# @app.route("/dados.html")
# def contato():
#     return render_template("/dados.html")

# @app.route("/conheca.html")
# def quem_somos():
#     return render_template("conheca.html")





