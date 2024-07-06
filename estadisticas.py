import globales
import json
import math

def sueldo_liquido_mas_alto():
    todos_los_empleados = globales.leer_archivo_json("Listado.json")

    empleados_ordenados = sorted(todos_los_empleados, key=lambda x: x['sueldo_liquido'], reverse = True)

    for empleado in empleados_ordenados[:1]:
        print("Nombre:", empleado['nombre'])
        print("Sueldo", empleado['sueldo_liquido'])
        return

     
def sueldo_liquido_mas_bajo():
    todos_los_empleados = globales.leer_archivo_json("Listado.json")

    empleados_ordenados = sorted(todos_los_empleados, key=lambda x: x['sueldo_liquido'], reverse = False)

    for empleado in empleados_ordenados[:1]:
        print("Nombre:", empleado['nombre'])
        print("Sueldo", empleado['sueldo_liquido'])
        return


def Promedio_sueldos_liquidos():
    todos_los_empleados = globales.leer_archivo_json("Listado.json")

    cantidad = 0
    suma = 0
    

    for empleado in todos_los_empleados:
        suma += empleado['sueldo_liquido']
        cantidad += 1

    Promedio = suma /cantidad
    print("Promedio de sueldos: ", Promedio)
    
    
 
def media_geometrica():
    todos_los_empleados = globales.leer_archivo_json("Listado.json")

    cantidad = 0
    suma = 0

    for empleado in todos_los_empleados:
        suma += math.log(empleado['sueldo_liquido'])
        cantidad += 1   

    media = math.exp(suma /cantidad) 
    print("Media aritmetica de los sueldos: ", media) 
      



if __name__ == "__main__":
    sueldo_liquido_mas_alto()
    sueldo_liquido_mas_bajo()
    Promedio_sueldos_liquidos()
    media_geometrica()
