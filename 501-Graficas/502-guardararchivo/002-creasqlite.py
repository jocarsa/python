import requests
import sqlite3
import pandas as pd

#Descarga de archivo
##url = 'https://jocarsa.com/log/registros.csv'
##contenido = requests.get(url, allow_redirects=True)
##open('registros.csv', 'wb').write(contenido.content)
#Creación de base de datos
conn = sqlite3.connect('registros.sqlite')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS "registros" (
	"Identificador"	INTEGER,
	"epoch"	TEXT,
	"anio"	TEXT,
	"mes"	TEXT,
	"dia"	TEXT,
	"hora"	TEXT,
	"minuto"	TEXT,
	"segundo"	TEXT,
	"ip"	TEXT,
	"navegador"	TEXT,
	"pagina"	TEXT,
	"post"	TEXT,
	"get"	TEXT,
	"sesion"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);
''')

# load the data into a Pandas DataFrame
registros = pd.read_csv('registros.csv')
# write the data to a sqlite table
registros.to_sql('registros', conn, if_exists='append', index = False)







