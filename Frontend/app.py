from flask import Flask, render_template, request
import pandas as pd

app = Flask("__name__")

# Configuração do Jinja
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Configurar o caminho para a pasta de templates
app.template_folder = 'src/templates'

# Configurar o caminho para a pasta de arquivos estáticos
app.static_folder = 'src/static'

buttonType = ''
cidade = ''
data = []

def csv_to_json(arquivo_csv, cidade, ano):
    csv_path = app.static_folder + '\\arquivos\\'+ano+'\\'+arquivo_csv+'.csv'
    print(csv_path)

    df = pd.read_csv(csv_path)
    json_data = df.to_numpy()
    
    if cidade == 'Jacarei' :
        label = [row[0] for row in json_data]
        print('label: ', label)
    elif cidade == 'Taubate' :
        label = [row[3] for row in json_data]
    else:
        label = [row[2] for row in json_data]
    return label

#########
@app.route("/") # criando rotas com decorator
def home():
    return render_template("/home/home.html")

#######
@app.route("/dados", methods=['GET', 'POST'])
def dados():
    global buttonType
    global cidade
    
    if request.method == 'POST':
        buttonType = request.form.get('buttonType')
        

    return render_template("/dados/dados.html", resultado=buttonType)

##########
@app.route("/dados/consulta", methods=['GET', 'POST'])
def consulta():
    Consultas=['transtorno_respiratoria_com_complicação_sistemica','transtorno_respiratoria_sem_complicação_sistemica']
    Cidades= ['Jacarei','Sao Jose dos Campos','Taubate']
    Anos=['2019','2020','2021','2022']

    cidade = request.form.get('cidade')
    consulta = request.form.get('consulta')
    ano = request.form.get('ano')

    if request.method == 'POST':
        data = csv_to_json(consulta, cidade, ano)
        return render_template("/consulta/consulta.html", Consultas=Consultas, Cidades=Cidades, Anos=Anos, data = data)
    
    return render_template("/consulta/consulta.html", Consultas=Consultas, Cidades=Cidades, Anos=Anos)

##########
@app.route("/dados/procedimento", methods=['GET', 'POST'])
def procedimento():
    Procedimentos=['cardiopatias', 'aparelho_circulatorio']
    Cidades= ['Jacarei','Sao Jose dos Campos','Taubate']
    Anos=['2019','2020','2021','2022']

    cidade = request.form.get('cidade')
    procedimento = request.form.get('procedimento')
    ano = request.form.get('ano')

    if request.method == 'POST':
        data = csv_to_json(procedimento, cidade, ano)
        return render_template("/procedimento/procedimento.html", Procedimentos=Procedimentos, Cidades=Cidades, Anos=Anos, data = data)
    
    return render_template("/procedimento/procedimento.html", Procedimentos=Procedimentos, Cidades=Cidades, Anos=Anos)

###########
@app.route("/dados/tratamento", methods=['GET', 'POST'])
def tratamento():
    Tratamentos=['internacoes_gerais', 'internacoes_toracicas', 'aparelho_respiratorio', 'trombose']
    Cidades= ['Jacarei','Sao Jose dos Campos','Taubate']
    Anos=['2019','2020','2021','2022']

    cidade = request.form.get('cidade')
    tratamento = request.form.get('tratamento')
    ano = request.form.get('ano')

    if request.method == 'POST':
        data = csv_to_json(tratamento, cidade, ano)
        return render_template("/tratamento/tratamento.html", Tratamentos=Tratamentos, Cidades=Cidades, Anos=Anos, data = data)
    
    return render_template("/tratamento/tratamento.html", Tratamentos=Tratamentos, Cidades=Cidades, Anos=Anos)


##########
@app.route("/quem_somos")
def quem_somos():
    return render_template("/quem_somos/quem_somos.html")


