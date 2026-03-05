from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# ACTIVIDAD 1
@app.get("/nombre")
def nombre():
    return {"nombre": "Juan Esteban Argüello Botero"}

@app.get("/universidad")
def universidad():
    return {"universidad": "CIAF"}

@app.get("/semestre")
def semestre():
    return {"semestre": "8vo semestre"}


# ACTIVIDAD 2
@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"mensaje": f"Hola {nombre}, Bienvenido"}

@app.get("/par_impar/{numero}")
def par_impar(numero: int):
    if numero % 2 == 0:
        return {"resultado": "Es par"}
    else:
        return {"resultado": "Es impar"}

@app.get("/edad/{anio}")
def calcular_edad(anio: int):
    año_actual = datetime.now().year
    edad = año_actual - anio
    return {"edad": edad}