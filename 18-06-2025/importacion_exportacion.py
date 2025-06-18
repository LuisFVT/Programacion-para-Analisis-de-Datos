import json

persona = {
    "nombre": "Juan",
    "edad": 30,
    "es_estudiante": False,
    "cursos": ["Programacion Para el Analisis de Datos", "Cibersueguridad"],
}

json_persona = json.dumps(persona, indent=4)

with open("persona.json", "w") as archivo:
    json.dump(persona, archivo, indent=4)   

print("Archivo 'persona.json' creado con éxito.")


with open("persona.json", "r") as archivo:
    persona_leida = json.load(archivo)
print("\nContenido Leido desde el archivo :")
print(persona_leida)    


#print("JSON")
#print(json_persona)

#persona_cargada = json.loads(json_persona)  
#print("\nDiccionario de nuevo:")
#print(persona_cargada)