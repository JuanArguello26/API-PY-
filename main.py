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



#Base de datos en memoria

estudiantes = [
    {"id": 1, "nombre": "Juan Esteban Argüello Botero"},
    {"id": 2, "nombre": "Stiven Arevalo Gutierrez"},
    {"id": 3, "nombre": "Maria Jose Henao Guerrero"},
]

@app.get("/estudiantes")
def obtener_estudiantes():
    return estudiantes

@app.get("/estudiante/{id}")
def obtener_estudiante(id: int):
    for estudiante in estudiantes:
        if estudiante["id"] == id:
            return estudiante
    return {"mensaje": "Estudiante no encontrado"}

@app.post("/estudiante")
def crear_estudiante(estudiante: dict):
    estudiantes.append(estudiante)
    return {"mensaje": "Estudiante creado exitosamente", "data": estudiante}

@app.put("/estudiante/{id}")
def actualizar_estudiante(id: int, estudiante: dict):
    for estudiante in estudiantes:
        if estudiante["id"] == id:
            estudiante["nombre"] = estudiante["nombre"]
            return {"mensaje": "Estudiante actualizado exitosamente", "data": estudiante}
    return {"mensaje": "Estudiante no encontrado"}

@app.delete("/estudiante/{id}")
def eliminar_estudiante(id: int):
    for estudiante in estudiantes:
        if estudiante["id"] == id:
            estudiantes.remove(estudiante)
            return {"mensaje": "Estudiante eliminado exitosamente"}
    return {"mensaje": "Estudiante no encontrado"}



