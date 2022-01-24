class Departamento:
    secuencia=0
    departamentos = []
    def __init__(self,descrip):
        Departamento.secuencia +=1
        self.codigo=Departamento.secuencia
        self.departamento=descrip

    def registro(self):
        return {"codigo":self.codigo,"descripcion":self.departamento}