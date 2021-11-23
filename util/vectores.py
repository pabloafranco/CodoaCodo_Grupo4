from random import randint

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y  = y
        self.z = z

    def sumar(vector1, vector2):
        salida=Vector(vector1.x+vector2.x, vector1.y+vector2.y,vector1.z+vector2.z)
        return(salida)

    def restar(vector1, vector2):
        return(Vector(vector1.x-vector2.x, vector1.y-vector2.y,vector1.z-vector2.z)        )

    def multiplicar(vector1, vector2):
        x = (vector1.y * vector2.z) - ( vector2.y * vector1.z)
        y = (vector1.x * vector2.z) - ( vector2.x * vector1.z)
        z = (vector1.x * vector2.y) - ( vector2.x * vector1.y)
        return(Vector(x,-y, z))

    def dividir(vector, escalar):
        x = (vector.x / escalar)
        y = (vector.y / escalar)
        z = (vector.z / escalar)
        return(Vector(x, y, z))

class Matriz:
    _n = 0
    _m = 0
    _elems = None

    def __init__(self, n, m, random):
        self._n = n
        self._m = m
        self._elems = []
        for i in range(n):
            self._elems.append([])
            for j in range(m):
                if random == "0":
                   self._elems[i].append(0)
                else:
                   self._elems[i].append(randint(0,10))

    def show_matrix(self):
        """ Imprime los valores almacenados en la matriz """
        for i in range(self._n):
            for j in range(self._m):
                # Imprime de una forma elegante la matriz
                print("| {0} ".format(self._elems[i], [j]), sep=',', end='')
            print('|\n')                

    def operacion(matriz1, matriz2, signo):
        matrizResultado=Matriz(3,3,"0")
        for a in range(3):
            for b in range(3):
                if signo=="+":
                    matrizResultado._elems[a][b] =  matriz1._elems[a][b] + matriz2._elems[a][b] 
                elif signo=="-":
                    matrizResultado._elems[a][b] =  matriz1._elems[a][b] - matriz2._elems[a][b] 
        
        
        return matrizResultado