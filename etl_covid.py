import requests  # librería para llamar la API
import pandas as pd

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
    
df = pd.DataFrame([data])

df.to_csv("data\covid_colombia.csv", index=False)