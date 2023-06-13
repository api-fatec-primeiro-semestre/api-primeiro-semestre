import json
import numpy as np
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
    covid_path = app.static_folder + '\\arquivos\\'+ano+'\\''casos_de_covid.csv' 

    df = pd.read_csv(csv_path)
    covid_df = pd.read_csv(covid_path)
    json_data = df.to_numpy()
    covid_json_data = covid_df.to_numpy()
    
    if cidade == 'Jacarei' :
        label = [row[0] for row in json_data]
        covid = [row[0] for row in covid_json_data]
        data = {
            'covid': covid,
            'grafico': label
        }
    elif cidade == 'Taubate' :
        label = [row[2] for row in json_data]
        covid = [row[2] for row in covid_json_data]
        data = {
            'covid': covid,
            'grafico': label
        }
    else:
        label = [row[1] for row in json_data]
        covid = [row[1] for row in covid_json_data]
        data = {
            'covid': covid,
            'grafico': label
        }
    return data
    

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
    options = {
        'cidades':[
            {
                'name': 'Jacareí',
                'value': 'Jacarei'  
            },
            {
                'name': 'São José dos Campos',
                'value': 'Sao Jose dos Campos'  
            },
            {
                'name': 'Taubaté',
                'value': 'Taubate'  
            },

        ],
        'consultas':[
            {
                'name':'Transtorno respiratória com complicação sistêmica',
                'value': 'transtorno_respiratoria_com_complicação_sistemica' 
            },
            {
                'name': 'Transtorno respiratória sem complicação sistêmica',
                'value':  'transtorno_respiratoria_sem_complicação_sistemica'
            }
        ],
        'anos':['2019','2020','2021','2022']
    }
    cidade = request.form.get('cidade')
    consulta = request.form.get('consulta')
    ano = request.form.get('ano')

    if request.method == 'POST':
        data = csv_to_json(consulta, cidade, ano)
        teste = consulta.replace('_', ' ')
        teste2 = json.dumps(teste)
        return render_template("/consulta/consulta.html", data = data, Options = options, Consulta=teste2)
    
    return render_template("/consulta/consulta.html", Options = options, data = [], consulta=consulta)

##########
@app.route("/dados/procedimento", methods=['GET', 'POST'])
def procedimento():

    options = {
        'cidades':[
            {
                'name': 'Jacareí',
                'value': 'Jacarei'  
            },
            {
                'name': 'São José dos Campos',
                'value': 'Sao Jose dos Campos'  
            },
            {
                'name': 'Taubaté',
                'value': 'Taubate'  
            },

        ],
        'procedimentos':[
            {
                'name':'Cardiopatias',
                'value': 'cardiopatias' 
            },
            {
                'name': 'Aparelho Circulatório',
                'value': 'aparelho_circulatorio'
            }
        ],
        'anos':['2019','2020','2021','2022']
    }

    cidade = request.form.get('cidade')
    procedimento = request.form.get('procedimento')
    ano = request.form.get('ano')
    
    if request.method == 'POST':
        data = csv_to_json(procedimento, cidade, ano)
        teste = procedimento.replace('_', ' ')
        teste2 = json.dumps(teste)
        return render_template("/procedimento/procedimento.html", Options = options, data = data, Procedimento=teste2)
    
    return render_template("/procedimento/procedimento.html", Options = options, data = [])

###########
@app.route("/dados/tratamento", methods=['GET', 'POST'])
def tratamento():

    options = {
        'cidades':[
            {
                'name': 'Jacareí',
                'value': 'Jacarei'  
            },
            {
                'name': 'São José dos Campos',
                'value': 'Sao Jose dos Campos'  
            },
            {
                'name': 'Taubaté',
                'value': 'Taubate'  
            },

        ],
        'tratamentos':[
            {
                'name':'Internações gerais',
                'value': 'internacoes_gerais' 
            },
            {
                'name': 'Internações torácicas',
                'value': 'internacoes_toracicas'
            },
            {
                'name': 'Aparelho respiratório',
                'value': 'aparelho_respiratorio'
            },
            {
                'name': 'Trombose',
                'value': 'trombose'
            }
        ],
        'anos':['2019','2020','2021','2022']
    }

    cidade = request.form.get('cidade')
    tratamento = request.form.get('tratamento')
    ano = request.form.get('ano')
    
    if request.method == 'POST':
        data = csv_to_json(tratamento, cidade, ano)
        teste = tratamento.replace('_', ' ')
        teste2 = json.dumps(teste)
        return render_template("/tratamento/tratamento.html", Options = options, data = data, Tratamento = teste2)
    
    return render_template("/tratamento/tratamento.html", Options = options, data = [])


##########
@app.route("/quem_somos")
def quem_somos():
    return render_template("/quem_somos/quem_somos.html")


