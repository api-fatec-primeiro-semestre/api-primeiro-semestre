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

@app.route("/dados", methods=['GET', 'POST'])
def dados():
    data=[
        ("JAN", 22,30),
        ("FEV", 25,20),
        ("MAR", 12, 42),
        ("ABR", 20,32),
        ("MAI", 78,60),
        ("JUN", 47,43),
        ("JUL", 50,71),
        ("AGO", 90,87),
        ("SET", 74,59),
        ("OUT", 78,71),
        ("NOV", 80,95),
        ("DEZ", 100,100),
    ]

    labels = [row[0] for row in data]
    values1 = [row[1] for row in data]
    values2 = [row[2] for row in data]

    Consultas=['Pneumologista','Cardiologista','Clinico Geral']
    Cidades= ['Jacareí','São José dos Campos','Taubaté']
    Anos=['2019','2020','2021','2022']
    
    global botao
    if request.method == 'POST':
        botao = request.form.get('botao')
    return render_template("/dados/dados.html", resultado=botao, labels=labels, values1=values1, values2=values2, Consultas=Consultas, Cidades=Cidades, Anos=Anos)

@app.route("/quem_somos")
def quem_somos():
    return render_template("/quem_somos/quem_somos.html")





