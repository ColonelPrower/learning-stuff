#Ejemplos del libro 
from cocos.director import director
from cocos.scene import Scene
from cocos.menu import *

class MiMenu(Menu):
    def __init__(self):
        super().__init__("Menu Principal")

        item1 = ToggleMenuItem('Sonido: ',self.eleccion_sonido, True)
        
        resoluciones = ['640x480','800x600','1024x768', '1600x900']
        item2 = MultipleMenuItem('Resolución: ',
                                self.eleccion_resolucion,
                                resoluciones)

        colores = [(255,0,0),(0,255,0),(0,0,255),(0,200,200)]
        item3 = MultipleMenuItem('Color: ',
                                 self.eleccion_color,
                                 str(colores))
        
        item4 = EntryMenuItem('Dificultad (1-10): ',
                                self.eleccion_dificultad,
                                '',
                                max_length=2)

        item5 = ImageMenuItem('mi_guerrero.png',
                                self.on_image_callback)
        item6 = MenuItem('Salir',self.salir)

        self.create_menu([item1,item2,item3,item4,item5,item6])

    def eleccion_sonido(self,encendido):
        if encendido:
            sel = 'activado'
        else:
            sel = 'desactivado'
        
        print(f"tu seleccion de audio esta: {sel}")
    
    def eleccion_resolucion(self,res):
        print(f"has elegido la opcion numero {res+1}")
    
    def eleccion_color(self,colorin):
        print(f"has elegido el color {colorin+1}")

    def eleccion_dificultad(self,difi):
        print(f"has elegido la dificultad {difi}")

    def on_image_callback(self):
        print("Has elegico comenzar el juego")
    
    def salir(self):
        director.window.close()
        print("haz elegid salir")

def main():
    ventana = director.init(width=800, height=600, caption='')
    ventana.set_location(500,200)
    director.run(Scene(MiMenu()))


if __name__ == '__main__':
    main()
