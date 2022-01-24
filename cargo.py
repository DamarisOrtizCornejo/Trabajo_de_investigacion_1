class Cargo:
    secuencia=2
    cargos = [{"codigo":1,"cargo":"Analista"},{"codigo":2,"cargo":"Jefe"}]
    def __init__(self,descrip):
        Cargo.secuencia +=1
        self.codigo=Cargo.secuencia
        self.descripcion=descrip

    def registro(self):
        return {"codigo":self.codigo,"cargo":self.descripcion}

    # def mostrar(self):
    #     print("{} - {}".format(self.codigo,self.descripcion))

    # def datos(self):
    #     return [self.codigo,self.descripcion]


# listaCategorias = []
# cat = Categoria("Lacteos")
# cat.mostrar()
# print(cat.datos())
# cat2 = Categoria("Bebidas")
# cat2.mostrar()
# print(cat2.datos())
# # listaCategorias.append(cat.datos())
# # listaCategorias.append(cat2.datos())
# cat = Categoria("Legumbres")
# Categoria.categorias.append(cat.registro())
# cat = Categoria("Carnes")
# Categoria.categorias.append(cat.registro())
# print(Categoria.categorias)
# listaCategorias.append(cat2.registro())
# listaCategorias.append(cat3.registro())
# print(listaCategorias)
