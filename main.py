#Librerias
from datetime import datetime
import requests
import pandas as pd
from pandas import json_normalize
import json

#Libreria agregada
#import os

#API
base_url = "https://api.openweathermap.org/data/2.5/weather?"

#Ciudades a buscar 
cityList = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"]

coordList = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]

api_key = "cfc35e951443dc18490d3fe2188e7267"#Esta key deberia ser llamada desde otro archivo

#Variable donde vamos a almacenar los registros
total_registros = []


def registros(ciudad, coordenadas):
    #url_completa = f"{base_url}q={ciudad}&appid={api_key}&units=metric"
    url_completa = f"{base_url}{coordenadas}&appid={api_key}&units=metric" 

    #Request a la api 
    response = requests.get(url_completa).json()
    
    #Obteniendo datos de interes 
    dt_value = response['dt']
    descripcion = response['weather'][0]['description']
    temperatura = response['main']['temp']
    temperatura_min = response['main']['temp_min']
    temperatura_max = response['main']['temp_max']
    sensacion_termica = response['main']['feels_like']
    humedad = response['main']['humidity']
    velocidad_viento = response['wind']['speed']

    return {"City Name": city,"Date": dt_value, "Descripcion Del Tiempo": descripcion, "Temperatura": temperatura, "Temperatura Min": temperatura_min, "Temperatura Max": temperatura_max, "Sensacion Termica": sensacion_termica, "Humedad": humedad, "Velocidad Viento": velocidad_viento}


#Control de ejecucion 
if __name__ == '__main__':
    for city, coordenadas in zip(cityList, coordList):
        data = registros(city, coordenadas)
        total_registros.append(data)

    #Paso los datos obtenidos a un DATAFRAME
    df = pd.DataFrame(total_registros)

    #Registrando la fecha de ejecucion
    fecha_actual = datetime.now().strftime("%Y%m%d")

    
    # Obtener la ruta absoluta
    path_file = f'data_analytics/openweather/tiempodiario_{fecha_actual}.csv'
    #absolute_path = os.path.abspath(path_file)

    #archivando datos
    with open(path_file, 'w') as output_file:
        df.to_csv( output_file, index=False)





