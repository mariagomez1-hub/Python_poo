class coordenada:
    # Metodo constructor
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def mostrarCoordenada(self):
        print("(",self.X,",",self.Y, ")")

    # Metodo de acceso
    def getX(self):
        return self.__X

    def setX(self, x):
        self.__X = x

    def getY(self):
        return self.__Y
    
    def setY(self, y):
        self.__Y = y
    
    #Metodo para mostrar la coordenada
    def mostrarCoordenadas(self):
        print("(",self.__X,",",self.__Y, ")")
