#Mini proyecto 1
#Objetivo: Consumir una API diaria, y generar un CSV incremental que registra casos diarios

import requests  # librería para llamar la API
import pandas as pd
from datetime import date
import os

# Paso 1: Hacer la solicitud
url = "https://disease.sh/v3/covid-19/countries/Colombia"
response = requests.get(url)

# Paso 2: Verificar si funcionó
if response.status_code == 200:
    data = response.json()  # convierte la respuesta a un diccionario de Python
    print("Casos confirmados:", data["cases"])
    print("Muertes:", data["deaths"])
    print("Recuperados:", data["recovered"])
else:
    print("Error al consultar la API:", response.status_code)
    
data["fecha"] = date.today().isoformat()
    
df = pd.DataFrame([data])

file_path = "data/historico_covid.csv"
df.to_csv(file_path, mode="a", header=not os.path.exists(file_path), index=False)

