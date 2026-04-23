# Poo en python
Introduccion a la programacion orientada en objetos(poo) en python

## ¿Por que aprender POO?

- Imagina que quieres crear un videojuego. Tienes guerreros, magos, dragones... cada uno con sus propios puntos de vida, ataques y habilidades. ¿Como los organizo en codigo sin repetir todo una y otra vez?

- La **Programacion Orientada a Objetos (POO)** es la respuesta. En lugar de escribir instrucciones sueltas, modelas el mundo real con *objetos* que tienen caraceristicas y comportamientos. Es la forma en que estan construidos la mayoria de los programas profesionales del mundo.

![POO](img/poo.png "POO")

## Clase y objeto

- Una clase es un tipo de dato cuyas variables se llaman objetos o instancias.

- La clase es la definicion del concepto del mundo real y los objetos o instancias son el propio "objeto" del mundo real.

- Las clases estan compuestas por dos elementos:
    - **Atributos:** informacion que almacena la clase.
    - **Metodos:** Operaciones que pueden realizarse con la clase.

## Definicion de una clase en python

``` Python
class NombreClase:
    
    def __init__(self, variable1, variable2):
        self.atributo1 = valor1
        self.atributo2 = valor2

        def nombreMetodo(self):
            BloqueCodigo
```
- `class` : palabra reservada en python para definir una clase.
- `NombreClase` : nombre de la clase que se quiere crear.
- `def` : palabra reservada en python que se utiliza para definir tanto al constructor de la clase (metodo que se ejecuta la primera vez que usas una clase) como diferentes metodos que tiene.
- `__init__`: palabra reservada en python para definir el tema constructor de la clase. El metodo `__init__` es lo primero que se ejecuta cuando creas un objeto de una clase.
- `(self, variableX)`: parámetro del constructor de la clase. El paramétro `self` es obligatorio y despues de tener tantos paramétros como quieras. La forma de añadir paramétros es la misma que en las funciones.
- `self.AtributoX`: forma de utilizacion y acceso a los atributos de la clase.
- `nombreMetodo`: nombre del metodo de la clase.
- `self`: paramétro del metodo. El paramétro `self`es obligatorio y despues puedes tener tantos paramétros como quieras. La forma de añadir paramétros es la misma que en las funciones.
- `BloqueCodigo`: instrucciones que se ejecutará el metodo.

**Al definir una clase tenga en cuenta:**
- Puedes definir tantos atributos como necesites.
- Puedes definir tantos metodos como necesites.
- Puedes definir tantos parametros en el constructor y en los metodos como necesites.

## Ejemplo 1

- Crear una clase que represente una persona.
- Atributos: nombre, apellidos y edad.
- Metodos: mostrar la informacion de la persona.

### Codigo

```Python
class Persona:

    # Metodo constructor de la clase
    def__init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    # Metodo para mostrar la informacion 
    def mostrarPersona(self):
        print("Nombre: ", self.nombre)
        print("Apellidos : ", self.apellidos)
        prinr("Edad: ", self.edad)

def main():
    print("vamoss a aprender POO...")
    persona_1 = Persona("Lorenzo", "Perez", "18")
    persona_1.mostrarPersona() 

if __name__ == main():
    main()
```
## Representacion en RAM del objeto creado

![Objeto RAM](img/objetoRAM.png "Objeto RAM")