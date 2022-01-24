# import os
# os.system("cls")
class Calculo:
  pass

class Helper:
  def __init__(self):
    x=10
    pass
  def menu(self,opciones,titulo):
    print(titulo)
    for opcion in opciones:
      print(opcion)
    opc = input("\033[0;37m"+"Elija Opcion[1...{}]: ".format(len(opciones)))
    return opc

# help = Helper()
# opcion = help.menu(["1) Primo","2) Fibonacci","3) Amigos","4) Salir"],"Menu Ejercicios")
# print(opcion)

