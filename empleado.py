from cargo import Cargo
from departamento import Departamento

class Empleado:
  secuencia=1
  Empleados = [ {"codigo":1,"nombre":"Dan","cedula":"0914192182","cargo":1,"departamento":1,"sueldo":500.00}]

  def __init__(self,nombre,cedula,codCargo,codDepartamento,sueldo ):
    Empleado.secuencia +=1
    self.codigo=Empleado.secuencia
    self.nombre=nombre
    self.cedula=cedula
    self.cargo=codCargo
    self.departamento=codDepartamento
    self.sueldo=sueldo

  # def mostrar(self):
  #   print("{} - {} - {} - {} - {} ".format(self.codigo,self.nombre,self.cedula,self.cargo,self.departamento,self.sueldo))

  def registro(self):
    return {"codigo":self.codigo,"nombre":self.nombre,"cedula":self.cedula,"cargo":self.cargo,"departamento":self.departamento,"sueldo":self.sueldo}
#print(Articulo.articulos)

# art = Articulo("Pepsi",2,1.5,100)
# #art.mostrar()
# articulo = art.registro()
# #print(articulo)
# Articulo.articulos.append(articulo)
# print(Articulo.articulos)