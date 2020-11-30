#Primero se importa Flask con pip install flask
#Flask es un “micro” Framework escrito en Python y concebido para facilitar el desarrollo de Aplicaciones Web.
from flask import Flask
#pandas es un paquete de Python que proporciona estructuras de datos similares a los dataframes de R.
import pandas as pd
#crear la aplicación Flask.
app = Flask(__name__)
#Ahora vamos a indicar que este método será el que atienda a las peticiones de la raíz de nuestro servidor
@app.route('/')
#Definimos la funcion
def tablaCSV():
    #pandas convierte el archivo csv en una tabla (DataFrame)
    readcsv = pd.read_csv('../data/employees.csv')
    #Ya que flask no soporta DataFrames lo converti en una tabla de html con el metodo .to_html()
    table = "<style> h1{font-family: Verdana;  } table, table th{ border-collapse:collapse;text-align:center; } </style>" + "<h1>Evaluación Shei Miceli</h1>" + readcsv.to_html()
    return(table)

if __name__== '__main__':
#lanzamos la aplicación mediante el método .run().
    app.run(debug=True)