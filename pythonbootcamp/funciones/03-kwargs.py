"""
keyword arguments
"""
def get_product(**datos): #2 asteriscos por kwargs
    print(datos)
    print(datos["desc"])

get_product(id="23",name="iPhone",desc="un telefono bien caro y feo") #retorna un dict
