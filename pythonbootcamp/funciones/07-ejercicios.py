"""
Ejercicios
"""
def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_reves = ""
    for char in texto:
        texto_reves = char + texto_reves

    return texto_reves


def es_palindromo(texto):
    texto = no_space(texto)
    inverso = reverse(texto)

    return True if texto.lower() == inverso.lower() else False

print("Abba", es_palindromo("Abba"))
print("Reconocer",es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola mundo", es_palindromo("Hola mundo"))
