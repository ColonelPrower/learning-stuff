"""
Comparado objetos
"""
class Coordenadas:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon


    def __eq__(self,otrains):
        return self.lat == otrains.lat and self.lon == otrains.lon

    def __ne__(self,otrains):
        return self.lat != otrains.lat or self.lon != otrains.lon
    
    def __lt__(self,otrains): #less than
        pass
    
    def __le__(self,otrains): #less or equal
        pass

coords = Coordenadas(45,27)
coords2 = Coordenadas(45,27)

# print(coords == coords2) #imprime false por el numero de espacio de memoria a menos que use el metodo __eq__ 
print(coords == coords2)
print(coords != coords2)# __ne__ no equal
