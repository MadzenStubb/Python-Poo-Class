import random

class Persona:
    underWeight = -1
    idealWeight = 0
    overWeight = 1

    def __init__(self, name=None, age=0, DNI=None, sex='H', weight=0.0, height=0.0):
        self.__name = name
        self.__age = age
        self.__DNI = self.generarDNI() if DNI is None else DNI
        self.__sex = self.comprobarSexo(sex)
        self.__weight = weight
        self.__height = height

    def calcularIMC(self):
        if self.__height <= 0:
            return None
        bmi = self.__weight / (self.__height ** 2)
        
        if bmi < 20:
            return self.underWeight
        elif 20 <= bmi <= 25:
            return self.idealWeight
        else: 
            return self.overWeight
        
    def esMayorDeEdad(self):
        return self.__age >= 18
    
    def comprobarSexo(self, sex):
        if sex in ['H', 'F']:
            return sex
        elif sex not in ['H', 'F']:
            return 'Sexo no especificado correctamente'
    
    def toString(self):
        return (f"Nombre: {self.__name}\n Edad: {self.__age} años\n DNI: {self.__DNI}\n Sexo: {self.__sex}\n Peso: {self.__weight}KG\n Altura: {self.__height}M")

    def generarDNI(self):
        number = random.randint(10000000, 99999999)
        letter = chr(65 + (number % 23))
        return f"{number}{letter}"
    
    def setName(self, name):
        self.__name = name
        
    def setAge(self, age):
        self.__age = age
        
    def setWeight(self, weight):
        self.__weight = weight
        
    def setHeight(self, height):
        self.__height = height
        
    def setSex(self, sex):
        self.__sex = self.comprobarSexo(sex)
        
    def mainConstructor():
        name = input("Ingrese su nombre: ")
        age = int(input("Ingrese su edad: "))
        sex = input("Ingrese su sexo: ")
        weight = float(input("Ingrese su peso: "))
        height = float(input("Ingrese su altura: "))

    
        
        
persona01 = Persona(name="Gerardo", age=23, DNI=None, sex="H", weight=70.2, height=1.76)

persona02 = Persona(name="Luis", age=30, DNI=None, sex="H")
persona02.setWeight(80.0)
persona02.setHeight(1.85)

persona03 = Persona()
persona03.setName("Ana")
persona03.setAge(25)
persona03.setSex("F")
persona03.setWeight(55.0)
persona03.setHeight(1.60)


objects_list = [persona01, persona02, persona03]

for persona in objects_list:
    imc = persona.calcularIMC()
    
    if imc == persona.underWeight:
        imc_message = "Estás por debajo de tu peso ideal."
    elif imc == persona.idealWeight:
        imc_message = "Estás en tu peso ideal."
    else:
        imc_message = "Tienes sobrepeso."
    
    age_message = "Eres mayor de edad." if persona.esMayorDeEdad() else "No eres mayor de edad."
    
    print(f"{persona.toString()}\n{imc_message}\n{age_message}\n")