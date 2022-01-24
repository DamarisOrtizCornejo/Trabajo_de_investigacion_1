from helpers import Helper
from cargo import Cargo
from empleado import Empleado
from departamento import Departamento
import os
import time

def buscargo(cod):
    car = 0
    for pos in range(0,len(Cargo.cargos)):
        cargo = Cargo.cargos[pos]
        if cargo["codigo"] == cod:
            car = cargo["cargo"]
            break
    return car

def busdepartamento(cod):
    dep = 0
    for pos in range(0,len(Departamento.departamentos)):
        departamento = Departamento.departamentos[pos]
        if departamento["codigo"] == cod:
            dep = departamento["descripcion"]
            break
    return dep

helper = Helper()
lista = ["\033[0;34m"+"1) Cargo","2) Departamento","3) Empleados","4) Salir"]
opcion=""
while opcion != "4":
    os.system("cls")
    opcion = helper.menu(lista,"\033[1;32m"+"MENÚ FICHA PERSONAL")
    if opcion == "1":
        opc1=""
        while opc1 != "3":
            os.system("cls")
            opc1 = helper.menu(["\033[3;35m"+"1) Ingreso","2) Consulta","3) Salir"],"\033[3;33m"+"******************** MANTENIMIENTO DE CARGOS ********************")
            os.system("cls")
            if opc1 == "1":
                print("\033[0;31m"+"*"*20," INGRESO DE CARGOS ","*"*20)
                while True:
                    ncargo = input("\033[0;36m"+"Ingrese el cargo: ")
                    if len(ncargo) <= 20 and len(ncargo) >0:
                        print("\033[3;37m"+"Datos ingresados correctamente")
                        break
                    else:
                        print("\033[3;37m"+"Maximo de 1 - 20 caracteres, ingrese nuevamente")
                        time.sleep(1)
                        os.system("cls")
                cargo1 = Cargo(ncargo)
                cargo2 = cargo1.registro()
                Cargo.cargos.append(cargo2)
                input("Presione una tecla para continuar...")
            elif opc1 == "2":
                print("\033[0;31m"+"*"*20,"LISTADO DE CARGOS","*"*20)
                print("\033[1;32m"+"Codigo"," "*5,"Descripcion")
                for cargo1 in Cargo.cargos:
                    cod = cargo1["codigo"]
                    des = cargo1["cargo"]
                    print(" "*2,cod," "*8,des)
                input("\033[3;37m"+"Presione una tecla para continuar...")

    elif opcion == "2":
        opc2=""
        while opc2 != "3":
            os.system("cls")
            opc2 = helper.menu(["\033[3;35m"+"1) Ingreso","2) Consulta","3) Salir"],"\033[3;33m"+"******************** MANTENIMIENTO DE DEPARTAMENTOS ********************")
            os.system("cls")
            if opc2 == "1":
                print("\033[0;31m"+"*"*20," INGRESO DE DEPARTAMENTOS ","*"*20)
                while True:
                    ndepartamento = input("\033[0;36m"+"Ingrese el departamento: ")
                    if len(ndepartamento) <= 20 and len(ndepartamento) >=5:
                        print("\033[3;37m"+"Datos ingresados correctamente")
                        break
                    else:
                        print("\033[3;37m"+"Maximo de 5 - 20 caracteres, ingrese nuevamente")
                        time.sleep(1)
                        os.system("cls")
                depar = Departamento(ndepartamento)
                depart = depar.registro()
                Departamento.departamentos.append(depart)
                input("Presione una tecla para continuar...")
            elif opc2 == "2":
                print("\033[0;31m"+"*"*20,"LISTADO DE DEPARTAMENTOS","*"*20)
                print("\033[1;32m"+"Codigo"," "*5,"Descripcion")
                for depar in Departamento.departamentos:
                    cod = depar["codigo"]
                    des = depar["descripcion"]
                    print(" "*2,cod," "*8,des)
                input("\033[3;37m"+"Presione una tecla para continuar...")

    elif opcion == "3":
        opc3=""
        while opc3 != "3":
            os.system("cls")
            opc3 = helper.menu(["\033[3;35m"+"1) Ingreso","2) Consulta","3) Salir"],"\033[3;33m"+"******************** MANTENIMIENTO DE EMPLEADOS ********************")
            os.system("cls")
            if opc3 == "1":
                print("\033[0;31m"+"*"*20," INGRESO DE EMPLEADOS ","*"*20)
                while True:
                    nombreE = input("\033[0;36m"+"Nombre: ")
                    if len(nombreE) <= 20 and len(nombreE) >=3:
                        break
                    else:
                        print("\033[3;37m"+"Maximo de 3 - 20 caracteres, ingrese nuevamente")
                        time.sleep(1)
                        os.system("cls")
                cedula= input("\033[0;36m"+"Cédula: ")
                cargo = int(input("\033[0;36m"+"Cargo: "))
                departamento = int(input("\033[0;36m"+"Departamento: "))
                sueldo= float(input("\033[0;36m"+"Sueldo: "))
                emp = Empleado(nombreE,cedula,cargo,departamento,sueldo)
                emple = emp.registro()
                Empleado.Empleados.append(emple)
                input("\033[3;37m"+"Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
            elif opc3 == "2":
                print("\033[1;31m"+"*"*40,"LISTADO DE EMPLEADOS","*"*40)
                print("\033[0;32m"+"Codigo"," "*5,"Nombre"," "*12,"Cedula"," "*10,"Cargo"," "*6,"Departamento "," "*8,"Sueldo")
                for emp in Empleado.Empleados:
                    cod = emp["codigo"]
                    nom = emp["nombre"]
                    ced = emp["cedula"]
                    car =emp["cargo"]
                    card = buscargo(car)
                    dep = emp["departamento"]
                    depd = busdepartamento(dep)
                    sue = emp["sueldo"]
                    print(" "*2,cod," "*8,nom," "*(15-len(nom)),ced," "*(17-len(ced)),card," "*(15-len(card)),depd," "*(8-len(depd))," "*10,sue)#sue," "*(20-len(str(sue))))
                input("\033[3;37m"+"Presione una tecla para continuar...")

    elif opcion == "3":
        print("Salir")

print("\033[3;35m"+"Gracias por visitarnos")
#print(Articulo.articulos)