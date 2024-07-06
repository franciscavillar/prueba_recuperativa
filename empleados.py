import globales
import json
import random

def asignar_valores():
    empleados = [
     "Luisa Morales",
     "Javier Torres",
     "Sofía Ramírez",
     "Martín Gutiérrez",
     "Valeria Castillo",
     "Diego Vargas",
     "Camila Ruiz",
     "Alejandro Medina",
     "Carolina Herrera",
     "Andrés Silva",
     "Paula Ortiz",
     "Gabriel Ramos"
    ]

    todos_los_empleados = []
 
    for nombre in empleados:
        Calculo_Sueldo_liquido = random.randint(90000, 150000) * 100
        calculo_salud = Calculo_Sueldo_liquido * 0.7
        calculo_afp = Calculo_Sueldo_liquido * 0.12

        nuevo_empleado = {
	        "nombre": nombre,
	        "salud": calculo_salud,
	        "afp":	calculo_afp,
	        "sueldo": Calculo_Sueldo_liquido
             }
        todos_los_empleados.append(nuevo_empleado)
    globales.guardar_archivo_json("Listado.json", todos_los_empleados)    


if __name__ == "__main__":
    asignar_valores()     




