#Librerias
from datetime import datetime
import requests
import pandas as pd
from pandas import json_normalize
import json
from config import api_key

#API
"""
Se puede llamar a la API de 2 formas
-Llamada con coordenadas
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

- Llamada con el nombre de la city
https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key} 

Para llamar a la API, uso el Nombre de las ciudades porque las coordenadas no son exactas al no tener los num despues de la coma, y termina trayendo datos de otras ciudades. A modo de mostracion dejo ambas formas de hacerlo.
Hice 2 cambios en cityList "Mexico DF" >> 'Mexico City' y "Tilfis" >> 'Tiflis'"""

base_url = "https://api.openweathermap.org/data/2.5/weather?"

#Ciudades a buscar 
cityList = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico City", "Dublin", "Tiflis", "Bogota", "Tokio"]

coordList = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]


#Variable donde vamos a almacenar los registros
#total_registros_coordenadas = []
total_registros_city = []

#Funcione que obtiene los datos de la API
def obtener_registros():
    for city, coordenadas in zip(cityList, coordList):
        url_completa = f"{base_url}q={city}&appid={api_key}&units=metric"
        #Request a la API y guardamos cada requests en una lista
        response = requests.get(url_completa).json()
        total_registros_city.append(response)

        #En caso de querer usar coordenadas 
        #url_completa2 = f"{base_url}{coordenadas}&appid={api_key}&units=metric"
        #response2= requests.get(url_completa2).json()
        #total_registros_coordenadas.append(response2)

        
#Pasamos los registros a DATAFRAME
def transformando_datos():
    df = pd.json_normalize(total_registros_city) 
    
    df = df.drop(['weather', 'base', 'sys.type', 'sys.id', 'cod','main.temp_max', 'main.temp_min', 'id'], axis=1)
    df.rename(columns = {'dt':'datetime','timezone':'timezone offset', 'name': 'city name','coord.lon':'longitud' ,'coord.lat' :'latitud', 'main.temp':'temperature', 'main.feels_like':'feels Like', 'main.pressure':'pressure', 'main.humidity':'humidity', 'main.sea_level':'Sea Level', 'wind.speed': 'wind speed', 'wind.deg': 'wind deg', 'wind.gust': 'wind gust', 'clouds.all': 'clouds', 'sys.country': 'country', 'sys.sunrise': 'sunrise','sys.sunset': 'sunset'}, inplace = True)

    datecols = ['datetime', 'sunrise', 'sunset']
    df[datecols] = df[datecols].apply(lambda x: pd.to_datetime(x, unit='s').dt.date)
    
    #Ejemplo del df2
    #df2 = pd.json_normalize(total_registros_coordenadas) 
    #df2 = df2.drop(['weather', 'base', 'sys.type', 'sys.id', 'cod','main.grnd_level','main.temp_max', 'main.temp_min', 'id'], axis=1)
    #df2.rename(columns = {'dt':'datetime','timezone':'timezone offset', 'name': 'city name','coord.lon':'longitud' ,'coord.lat' :'latitud', 'main.temp':'temperature', 'main.feels_like':'feels Like', 'main.pressure':'pressure', 'main.humidity':'humidity', 'main.sea_level':'Sea Level', 'wind.speed': 'wind speed', 'wind.deg': 'wind deg', 'wind.gust': 'wind gust', 'clouds.all': 'clouds', 'sys.country': 'country', 'sys.sunrise': 'sunrise','sys.sunset': 'sunset'}, inplace = True) 

    return df 

#Control de ejecucion 
if __name__ == '__main__':
    #ejecutando funciones:
    obtener_registros()
    df = transformando_datos()
    
    #Registrando la fecha de ejecucion
    fecha_actual = datetime.now().strftime("%Y%m%d")

    #Ruta donde almacenaremos el archivo y su fecha
    path_file = f'data_analytics/openweather/tiempodiario_{fecha_actual}.csv' 

    #archivando datos
    with open(path_file, 'w') as output_file:
        df.to_csv(output_file, encoding="UTF8", sep=",", index=False)
        print(df)




