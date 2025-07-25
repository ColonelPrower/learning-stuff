edad = int(input("edad: "))

if edad > 17:
    mensaje = "Es mayor"
else:
    mensaje = "Es menor"

print(mensaje)

mensaje2 = "Es mayor" if edad > 17 else "Es menor"

print(mensaje2)

