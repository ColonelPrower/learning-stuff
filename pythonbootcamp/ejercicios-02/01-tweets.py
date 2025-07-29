"""
Verificador de tweets
"""
tweetchars = 20
tweet = input("En que estas pensando? ")

if tweet:
    print("Su tweet ha sido publicado" if len(tweet) < tweetchars else "Ha sobrepasado el limite de su publicacion" )
else:
    print("No se puede publicar un tweet vacio")
