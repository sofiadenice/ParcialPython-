import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
def suma():
    result = 2 + 4
    return result


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros pares del 1 al 1000
"""


# start-->
def sumaPares(rango):
    sumatotal = 0
    i = 0
    sumatotal = 0
    while i <= int(rango):
        if (i %2 == 0):
            sumatotal += i
        i += 1
    return sumatotal


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area total de superficie de un cilindro
radio = 5 m
altura = 7 m
area lateral: 2*pi*r*a
area circulo: 2*pi*r^2
area total: area lateral + area circulo
"""


# start-->
def _init_(self, radio, altura):
        
        self.radio = radio
        self.altura = altura
        
        def areaTotalCilindro(self):
            result = round(areaLateral(self.radio,self.altura) + areaCirculo(self.radio),2)
            return result

        def areaLateral(self):
            result = 2.0*math.pi*self.radio*self.altura
            return result

        def areaCirculo(self):
            result = 2.0*math.pi*self.radio**2
            return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cilindro:
 
    def _init_(self, radio, altura):
        
        self.radio = radio
        self.altura = altura
        
    def areaTotalCilindro(self):
        result = round(areaLateral(self.radio,self.altura) + areaCirculo(self.radio),2)
        return result

    def areaLateral(self):
        result = 2.0*math.pi*self.radio*self.altura
        return result
    def areaCirculo(self):
        result = 2.0*math.pi*self.radio**2
        return result

"""
***************************************************************
@@ ejercicio 5 @@
restaurante de pizzas
pizza
    nombre
    lugar
    costo
    conDescuento
    descuento
"""


class Restaurante:
    def ordenar(self):
        pass

    def costoTotal(self):
        return 0

    def costoTotalConDescuento(self):
        return 0


class Pizza:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
