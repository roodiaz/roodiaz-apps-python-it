import requests
import pandas as pd
import statistics

r = requests.get("https://api.recursospython.com/dollar")
cotizacion = statistics.mean(r.json().values())

print(cotizacion)

def dolar_a_peso(precio_en_usd):
    return precio_en_usd * cotizacion

excel = pd.read_excel("productos.xlsx")
excel["Precio en pesos"] = excel["Precio en dólares"].apply(dolar_a_peso)
excel.to_excel("productos_pesificados.xlsx", index=False)
