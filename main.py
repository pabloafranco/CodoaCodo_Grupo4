import util
from util.funciones import *
import util
from util.complejos import *
import util
from util.vectores import *


ans=True
while ans:
    print("""
    1.Dado un string, cambiar todos los espacios por guiones.('Esto es  una prueba', ' ', '-')
    2.Cambiar Mayusculas por Minusculas.("Esto cambia Mayusculas por minusculas y viceversa")
    3.Recibir string, indice y letra a modificar y devuelve string modificado.('Cambiar una Letra', 12, 'l')
    4.Devuelva un string con el nombre y apellido pero con capitalizacion.("veamos esta prueba si funciona bien")
    5.Devuelve la puntuacion del subcampeon,([3,4,42,1,4,621,621,620,3,5])
    6.(5a)Recibe un numero entero y imprima  un triangulo de numeros de altura. (impTriangulo(13))
    7.(5b)reciba string, devolver 3 caracteres mas usados en orden descendiente.(caracterMasUsado("Codo a codo", True))
    8.Sumar complejos (20,1) + (11,45)
    9.Restar complejos (10,18) + (8,45)
    10.Multiplicar complejos (2,4) * (3,-2)
    11.Sumar dos vectores A = (2;1;−2) B = (1;-3;1) 
    12.Restar dos vectores A = (4;-8;6) B = (1;4;2) 
    13.Multiplicar dos vectores A = (1;2;3) B = (4;5;6) 
    14.Dividir vector por escalar A = (4;6;8) escalar 2
    15.Sumar 2 Matriz de (3x3)  
    16.Restar 2 Matriz de (3x3)  
    17.Multiplicar Matriz de (3x3)  x Vector de (3x1) (Sin hacer)
    99.Exit/Quit
    """)
    ans=input("Que quiere hacer? ")
    if ans=="1":
        # caso 1
        print ("Caso 1")
        texto=input("Texto a Reemplazar: ")
        print (reemplazar(texto, ' ', '-'))
    elif ans=="2":
        # caso 2
        texto=input("Texto a cambiar Mayusculas por minusculas y viceversa: ")
        print(mayPorMin(texto))
    elif ans=="3":
       # caso 3
       texto=input("Texto a cambiar una letra: ")
       indice=int(input("Indice: "))
       letra=input("Porque letra: ")
       print(cambioLetra(texto, indice, letra))
    elif ans=="4":
       # caso 4
       print ("Caso 4")
       texto=input("Pasar primera letra mayuscua: ")
       print(primeraLetraMay(texto))
    elif ans=="5":
       #caso 5
       print ("Caso 5")
       print (subCampeon([3,4,42,1,4,621,621,620,3,5]))
    elif ans=="6":
        #caso 5a
        triangulo=int(input("Numero a hacer triangulo: "))
        print ("Caso 5a")
        impTriangulo(triangulo)
    elif ans=="7":
        #caso 5b
        texto=input("Nombre de la empresa(caracter mas usado): ")
        nocase=input("Considera igual las mayuscualas/minusculas(S/N): ")
        if nocase.upper()=="S":
            lnocase=True
        else:
            lnocase=False
        caracterMasUsado(texto, lnocase)       
    elif ans=="8":        
        comple1 = Complejo(20,1) 
        comple2 = Complejo(11,45)
        resultado=Complejo.sumar(comple1,comple2)

        print (resultado.real, resultado.imaginario)

    elif ans=="9":        
        comple1 = Complejo(10,18)  
        comple2 = Complejo(8,45)
        resultado=Complejo.restar(comple1,comple2)

        print (resultado.real, resultado.imaginario)

    elif ans=="10":
        comple1 = Complejo(2,4)
        comple2 = Complejo(3,-2)
        resultado=Complejo.multiplicar(comple1,comple2)

        print (resultado.real, resultado.imaginario)

    elif ans=="11":
        a = Vector(2,1,-2)
        b = Vector(1,-3,1) 
        salida=Vector.sumar(a,b)
        print (salida.x, salida.y, salida.z)

    elif ans=="12":
        a = Vector(4,-8,6)
        b = Vector(1,4,2) 
        salida=Vector.restar(a,b)
        print (salida.x, salida.y, salida.z)

    elif ans=="13":
        a = Vector(1,2,3)
        b = Vector(4,5,6) 
        salida=Vector.multiplicar(a,b)
        print (salida.x, salida.y, salida.z)

    elif ans=="14":
        a = Vector(4,6,8)
        escalar = 2
        salida=Vector.dividir(a,escalar)
        print (salida.x, salida.y, salida.z)
    elif ans=="15":
        a = Matriz( 3, 3, "R")
        a.show_matrix()
        b = Matriz( 3, 3, "R")
        b.show_matrix()

        salida=Matriz.operacion(a,b,"+")

        salida.show_matrix()

    elif ans=="16":
        a = Matriz( 3, 3, "R")
        a.show_matrix()
        b = Matriz( 3, 3, "R")
        b.show_matrix()

        salida=Matriz.operacion(a,b,"-")

        salida.show_matrix()

    elif ans=="17":
        """"
        a = Matriz( 3, 3, "R")
        a.show_matrix()
        
        salida=Matriz.operacion(a,b,"-")

        salida.show_matrix()
        """

    elif ans=="99":
       print("\n Adios") 
       ans = None
    else:
       print("\n La opcion no es valda, intenet nuevamente.")









