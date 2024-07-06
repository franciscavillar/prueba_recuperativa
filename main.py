import os
import globales
import empleados
import estadisticas


def menu_general():
    while True:
     os.system("cls")
     print("===== MENU ====")
     print("1. Asignar sueldos aleatorios")
     print("2. Ver estadísticas")
     print("3. Salir del programa")

     opcion = globales.seleccionar_opcion(3)

     if opcion == 1:
        empleados.asignar_valores()
        print("SUELDO ALEATORIOS ASIGNADOS")
     elif opcion == 2:
        print("CARGANDO ESTADISTICAS")
        menu_estadisticas()
     elif opcion == 3:   
        os.system("cls")
        print("SALIENDO DEL SISTEMA . . .") 
        return
     input()
    
def menu_estadisticas():
    while True:
     os.system("cls")
     print("===== MENU ESTADISTICAS ====")
     print("1. Sueldo líquido más alto")
     print("2. Sueldo líquido más bajo")
     print("3. Promedio de sueldos líquido")
     print("4. Media geométrica sueldo líquido")
     print("5. Salir del menú estadisticas")

     opcion = globales.seleccionar_opcion(5)

     if opcion == 1:
        print("Sueldo líquido más alto")
        estadisticas.sueldo_liquido_mas_alto() 
     elif opcion == 2:
        print("Sueldo líquido más bajo")
        estadisticas.sueldo_liquido_mas_bajo()
     elif opcion == 3:
    
        estadisticas.Promedio_sueldos_liquidos()
     elif opcion == 4:
        
        estadisticas.media_geometrica()
     elif opcion == 5:   
        os.system("cls")
        print("SALIENDO DEL MENU ESTADISTICAS . . .") 
        return
     
     input()


if __name__ == "__main__":
    menu_general()    



