import random
import string


class Password:   
    def __init__(self, longitud=8, password=None):
        self.longitud = longitud
        self.password = password or self.generarPassword(self.longitud)

    def generarPassword(self, longitud):
        incDigits = input("¿Incluye dígitos? (si/no): ").lower() == 'si'
        incSC = input("¿Incluye símbolos especiales? (si/no): ").lower() == 'si'

        characters = string.ascii_letters
        if incDigits:
            characters += string.digits
        if incSC:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(self.longitud))
        return password
    
    def esFuerte(self, password):
        lower = set(string.ascii_lowercase).intersection(password)
        upper = set(string.ascii_uppercase).intersection(password)
        digits = set(string.digits).intersection(password)
        has_lower = len(lower) >= 1
        has_upper = len(upper) >= 2
        has_digit = len(digits) >= 5

        return has_lower and has_upper and has_digit
        

passwordDummy = Password()
print("Contraseña generada:", passwordDummy.password)
print("¿Su contraseña es fuerte?:", passwordDummy.esFuerte(passwordDummy.password))
