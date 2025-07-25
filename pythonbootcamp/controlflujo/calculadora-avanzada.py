
print("Bienvenido a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, multi, div, y resta")

num = input("Ingresa num: ")

while True: 
    op = input("Ingresa operacion: ")
    if op == "salir":
        break

    nextnum = input("Ingresa siguiente num: ")
    if nextnum == "salir":
        break

    match op:
        case "suma":
            num = int(num) + int(nextnum)
        case "resta":
            num = int(num) - int(nextnum)
        case "multi":
            num = int(num) * int(nextnum)
        case "div":
            num = int(num) / int(nextnum)

    print(f"El resultado es {num}")
