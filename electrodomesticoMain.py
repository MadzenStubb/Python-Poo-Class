from enum import Enum

COLOR_DEFAULT = "blanco"
PRECIO_BASE_DEFAULT = 100
PESO_DEFAULT = 5
CARGA_DEFAULT = 5
RESOLUCION_DEFAULT = 20
SINTONIZADOR_DEFAULT = False

class ConsumoEnergetico(Enum):
    A = 100
    B = 80
    C = 60
    D = 50
    E = 30
    F = 10

class Electrodomestico:
    validColors = ["blanco", "negro", "rojo", "azul", "gris"]

    def __init__(self, basePrice=PRECIO_BASE_DEFAULT, color=COLOR_DEFAULT,
                 consumoEnergetico=ConsumoEnergetico.F, weight=PESO_DEFAULT):
        self.basePrice = basePrice
        self.color = self.compColor(color)
        self.consumoEnergetico = self.compConsumEnergetico(consumoEnergetico)
        self.weight = weight

    def compConsumEnergetico(self, letra):
        return letra if letra in ConsumoEnergetico.__members__.values() else ConsumoEnergetico.F

    def compColor(self, color):
        return color.lower() if color.lower() in self.validColors else COLOR_DEFAULT
    
    def calcPrecioPorPeso(self):
        if self.weight < 20:
            return 10
        elif self.weight >= 20 and self.weight <= 49:
            return 50
        elif self.weight >= 50 and self.weight <= 79:
            return 50
        elif self.weight >= 80:
            return 100

    def precioFinal(self):
        precioFinal = self.basePrice + self.consumoEnergetico.value + self.calcPrecioPorPeso()
        return precioFinal

class Lavadora(Electrodomestico):
    def __init__(self, basePrice=PRECIO_BASE_DEFAULT, color=COLOR_DEFAULT,
                 consumoEnergetico=ConsumoEnergetico.F, weight=PESO_DEFAULT,
                 carga=CARGA_DEFAULT):
        super().__init__(basePrice, color, consumoEnergetico, weight)
        self.carga = carga

    def precioFinal(self):
        precioFinal = super().precioFinal()
        if self.carga > 30:
            precioFinal += 50
        return precioFinal

class Television(Electrodomestico):
    def __init__(self, basePrice=PRECIO_BASE_DEFAULT, color=COLOR_DEFAULT,
                 consumoEnergetico=ConsumoEnergetico.F, weight=PESO_DEFAULT,
                 resolucion=RESOLUCION_DEFAULT, sintonizador=SINTONIZADOR_DEFAULT):
        super().__init__(basePrice, color, consumoEnergetico, weight)
        self.resolucion = resolucion
        self.sintonizador = sintonizador

    def precioFinal(self):
        precioFinal = super().precioFinal()
        if self.resolucion > 40:
            precioFinal *= 1.3
        if self.sintonizador:
            precioFinal += 50
        return precioFinal

class Ejecutable:
    def __init__(self):
        self.electrodomesticos = [
            Lavadora(basePrice=300, weight=25),
            Television(basePrice=500, weight=10),
            Electrodomestico(basePrice=150),
            Lavadora(basePrice=200, weight=35),
            Television(basePrice=400, weight=15),
            Electrodomestico(basePrice=250),
            Lavadora(basePrice=350, weight=40),
            Television(basePrice=600, weight=20),
            Electrodomestico(basePrice=175),
            Lavadora(basePrice=450, weight=30),
        ]


    def calcular_precios(self):
        total_electrodomesticos = sum(electrodomestico.precioFinal() for electrodomestico in self.electrodomesticos)
        
        total_lavadoras = sum(electrodomestico.precioFinal() for electrodomestico in self.electrodomesticos if isinstance(electrodomestico, Lavadora))
        
        total_televisiones = sum(electrodomestico.precioFinal() for electrodomestico in self.electrodomesticos if isinstance(electrodomestico, Television))
        
        print(f"Precio total Electrodomésticos: ${total_electrodomesticos:.2f}")
        print(f"Precio total Lavadoras: ${total_lavadoras:.2f}")
        print(f"Precio total Televisiones: ${total_televisiones:.2f}")
        
if __name__ == "__main__":
    ejecutable = Ejecutable()
    ejecutable.calcular_precios()