import requests
import sqlite3
import pandas as pd
import matplotlib.pyplot as plot

#Descarga de archivo
url = 'https://jocarsa.com/log/registros.csv'
contenido = requests.get(url, allow_redirects=True)
open('registros.csv', 'wb').write(contenido.content)
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
cursor.execute('''
    DELETE FROM registros;
''')

# load the data into a Pandas DataFrame
registros = pd.read_csv('registros.csv', usecols=["epoch", "anio","mes","dia","hora","minuto","segundo","ip","navegador","pagina","post","get","sesion"], low_memory=False)

# write the data to a sqlite table
registros.to_sql('registros', conn, if_exists='append', index = False)

# Leer registros

cursor.execute('''
    SELECT COUNT(hora),hora
    FROM registros
    WHERE 
    
    navegador NOT LIKE '%bot%'
    AND
    navegador NOT LIKE '%spider%'
    AND
    navegador NOT LIKE '%crawl%'
    
    GROUP BY CAST(hora as decimal) 
''')
datos = cursor.fetchall()

horas = []
visitas = []

for i in datos:
    print("Visitas:",i[0],"\t hora:",i[1])
    if i[1] is not None:
        horas.append(i[0])
        visitas.append(i[1])


conn.commit()

print(horas)
print(visitas)

plot.bar(visitas, horas, align='center')
plot.ylabel('Horas')
plot.title('Visitantes cada hora')

plot.show()




