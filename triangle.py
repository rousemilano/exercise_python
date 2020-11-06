########################################
#Area triángulo usando la fórmula herón#
########################################

#Importando método del módulo math
from math import sqrt


class Triangle:
    #constructor
    def __init__(self, a, b, c):
        #atributos privados de los lados de un triangulo
        self.__a = a
        self.__b = b
        self.__c = c
        
    #Función que retorna el perimetro
    def perimeter(self):
        return self.__a + self.__b + self.__c

    #Función que retorna el semi perimetro
    def semiPerimeter(self):
        return (self.perimeter())/2
    
    #Función que retorna el area
    def area(self):
        s = self.semiPerimeter()
        return round(sqrt(s*(s-self.__a)*(s-self.__b)*(s-self.__c)),3)

#Instancia de la clase Triangle
myTriangle = Triangle(4,5,7)

#Acceso al método area e impresión de resultado
print("Area: ",myTriangle.area())
