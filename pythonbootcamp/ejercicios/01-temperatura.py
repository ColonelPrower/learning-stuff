
temperatura = int(input("Ingresa la temperatura en °C: "))

faren = ((temperatura * 9)/5)+32
kelvin = temperatura + 273.15

msj = f"""
Temperatura de {temperatura}°C
Farenheit {faren}°F
Kelvin {kelvin}°K
"""
print(msj)