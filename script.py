
class Cliente:
    def __init__(self, nombre, dni, email, skype):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.skype = skype
        self.telefonos = []  # atributo NO obligatorio
        self.hijos = {}

    def contacto(self):         # metodo para mostrar información del contacto(en este caso el email y skype)
        texto = f"Email:{self.email} - Skype: {self.skype}"   #llamamos con el self para poder obtener la información
        return texto
    
    def agregar_telefono(self, telefono):   # nos permite agregar valores al array vacio de telefonos
        self.telefonos.append(telefono)

    def enviar_email(self, texto):
        print("Enviando email al cliente")

    def serialize(self):
        return{
            "nombre": self.nombre,
            "email": self.email,
            "telefonos": self. telefonos

        }
    
    def agregar_hijos(self, hijo):
        self.hijos.append(hijo)

    def buscar_hijos(self, nombre):   #buscamos un hijo en nuestra lita de hijos
        listado = []
        for hijo in self.hijos:
            if hijo['nombre'].upper() == nombre.upper():  # tmb ponemo if hijo.get('nombre') == nombre, el upper lo pasa todo a mayusculas para evitar diferencias de escritura
                listado.append(hijo)

            return listado



hijo = {
    "nombre": "pepe",
    "edad": 25
}

cliente_uno = Cliente(dni="111444J", nombre="Adrian",  email="4geeks@gmail.com", skype="@marco2342")


cliente_uno.agregar_telefono("610242838")
cliente_uno.enviar_email("Hola personas")

print(cliente_uno.serialize())

print(cliente_uno.telefonos)


"""
class Coche:  # Describimos como van a ser nuestros objetos
    def __init__(self, color, marca, modelo): 
        self.color = color
        self.marca = marca
        self.modelo = modelo      

    def __str__(self):
        return self.color
    
    def girar(self, direccion):  # metemos métodos
        return f"girando a la {direccion}"
  

coche_uno = Coche(color="rojo",marca="nissan", modelo="A2")
print(coche_uno)
print(coche_uno.marca)
print(coche_uno.modelo)
print(coche_uno.girar("izquierda"))

coche_dos = Coche(color="regro",marca="mercedes", modelo="AMG")
print(coche_dos)
print(coche_dos.marca)
print(coche_dos.modelo)

"""