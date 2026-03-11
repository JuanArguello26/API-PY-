from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

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



# Models
class Estudiante(BaseModel):
    id: int
    nombre: str
    edad: Optional[int] = None
    correo: Optional[str] = None

class Profesor(BaseModel):
    id: int
    nombre: str
    materia: str
    experiencia: int

class Curso(BaseModel):
    id: int
    nombre: str
    profesor_id: int
    duracion_horas: int

# In-memory "Databases"
estudiantes_db = [
    {"id": 1, "nombre": "Juan Esteban Argüello Botero", "edad": 21, "correo": "juan@example.com"},
    {"id": 2, "nombre": "Stiven Arevalo Gutierrez", "edad": 22, "correo": "stiven@example.com"},
    {"id": 3, "nombre": "Maria Jose Henao Guerrero", "edad": 20, "correo": "maria@example.com"},
]

profesores_db = [
    {"id": 1, "nombre": "Carlos Perez", "materia": "Programación", "experiencia": 10},
]

cursos_db = [
    {"id": 1, "nombre": "FastAPI Masterclass", "profesor_id": 1, "duracion_horas": 40},
]

# CRUD ESTUDIANTES
@app.get("/estudiantes", tags=["Estudiantes"], summary="Obtener Estudiantes")
def obtener_estudiantes():
    return estudiantes_db

@app.get("/estudiantes/{id}", tags=["Estudiantes"], summary="Obtener Estudiante")
def obtener_estudiante(id: int):
    for e in estudiantes_db:
        if e["id"] == id:
            return e
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")

@app.post("/estudiantes", tags=["Estudiantes"], summary="Crear Estudiante")
def crear_estudiante(estudiante: Estudiante):
    estudiantes_db.append(estudiante.dict())
    return {"mensaje": "Estudiante creado exitosamente", "data": estudiante}

@app.put("/estudiantes/{id}", tags=["Estudiantes"], summary="Actualizar Estudiante")
def actualizar_estudiante(id: int, estudiante_data: Estudiante):
    for i, e in enumerate(estudiantes_db):
        if e["id"] == id:
            estudiantes_db[i] = estudiante_data.dict()
            return {"mensaje": "Estudiante actualizado exitosamente", "data": estudiante_data}
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")

@app.delete("/estudiantes/{id}", tags=["Estudiantes"], summary="Eliminar Estudiante")
def eliminar_estudiante(id: int):
    for i, e in enumerate(estudiantes_db):
        if e["id"] == id:
            estudiantes_db.pop(i)
            return {"mensaje": "Estudiante eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")


# CRUD PROFESORES
@app.get("/profesores", tags=["Profesores"], summary="Obtener Profesores")
def obtener_profesores():
    return profesores_db

@app.get("/profesores/{id}", tags=["Profesores"], summary="Obtener Profesor")
def obtener_profesor(id: int):
    for p in profesores_db:
        if p["id"] == id:
            return p
    raise HTTPException(status_code=404, detail="Profesor no encontrado")

@app.post("/profesores", tags=["Profesores"], summary="Crear Profesor")
def crear_profesor(profesor: Profesor):
    profesores_db.append(profesor.dict())
    return {"mensaje": "Profesor creado exitosamente", "data": profesor}

@app.put("/profesores/{id}", tags=["Profesores"], summary="Actualizar Profesor")
def actualizar_profesor(id: int, profesor_data: Profesor):
    for i, p in enumerate(profesores_db):
        if p["id"] == id:
            profesores_db[i] = profesor_data.dict()
            return {"mensaje": "Profesor actualizado exitosamente", "data": profesor_data}
    raise HTTPException(status_code=404, detail="Profesor no encontrado")

@app.delete("/profesores/{id}", tags=["Profesores"], summary="Eliminar Profesor")
def eliminar_profesor(id: int):
    for i, p in enumerate(profesores_db):
        if p["id"] == id:
            profesores_db.pop(i)
            return {"mensaje": "Profesor eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Profesor no encontrado")


# CRUD CURSOS
@app.get("/cursos", tags=["Cursos"], summary="Obtener Cursos")
def obtener_cursos():
    return cursos_db

@app.get("/cursos/{id}", tags=["Cursos"], summary="Obtener Curso")
def obtener_curso(id: int):
    for c in cursos_db:
        if c["id"] == id:
            return c
    raise HTTPException(status_code=404, detail="Curso no encontrado")

@app.post("/cursos", tags=["Cursos"], summary="Crear Curso")
def crear_curso(curso: Curso):
    cursos_db.append(curso.dict())
    return {"mensaje": "Curso creado exitosamente", "data": curso}

@app.put("/cursos/{id}", tags=["Cursos"], summary="Actualizar Curso")
def actualizar_curso(id: int, curso_data: Curso):
    for i, c in enumerate(cursos_db):
        if c["id"] == id:
            cursos_db[i] = curso_data.dict()
            return {"mensaje": "Curso actualizado exitosamente", "data": curso_data}
    raise HTTPException(status_code=404, detail="Curso no encontrado")

@app.delete("/cursos/{id}", tags=["Cursos"], summary="Eliminar Curso")
def eliminar_curso(id: int):
    for i, c in enumerate(cursos_db):
        if c["id"] == id:
            cursos_db.pop(i)
            return {"mensaje": "Curso eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Curso no encontrado")



