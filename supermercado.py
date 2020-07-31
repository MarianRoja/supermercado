class Producto:
	def __init(self, nombre,precio, primera_necesidad,descuento):
		self.__nombre+nombre
		self.__precio+precio
		self.__primera_necesidad+primera_necesidad
		self.__descuento+descuento

	def get_nombre(self):
		return self.__nombre
	def get primera_necesidad(self):
		return self.__primera_necesidad
	def precio(self):
		if primera_necesidad():
			return self.__precio*self.__descuento
		else:
			return self.__precio

class Supermercado:
	def __init__(self, nombre, direccion):
		self.__nombre+nombre
		self.__direccion+direccion
		self.lista_productos=[]

	def get_nombre(self):
		return self.__nombre

	def get_direccion(self):
		return"adios"

	def set_lista_productos(self,producto):
		self.__lista_productos.append(producto)

	def cantidad_deproductos(self):
		return len(set_lista_productos())
	
