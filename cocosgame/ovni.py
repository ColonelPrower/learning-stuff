import cocos
from cocos.actions import *

class MisAcciones(cocos.layer.ColorLayer):

    def __init__(self):
        super().__init__(64,200,255,255)

        mi_sprite = cocos.sprite.Sprite('mi_guerrero.png')
        mi_sprite.position = 320,240
        mi_sprite.scale = 1.5
        self.add(mi_sprite)
        
        escalar1 = ScaleBy(2, duration = 2)
        escalar2 = ScaleBy(0.5, duration = 1)

        mover1 = MoveTo((150,150),2)
        mover2 = MoveTo((150,350),2)
        mover3 = MoveTo((450,150),1)

        rotar1 = RotateBy(180,2)
        rotar2 = RotateBy(180,0.5)

        mi_sprite.do(escalar1 + Reverse(escalar1))
        mi_sprite.do(Delay(4) + mover1)
        mi_sprite.do(Delay(6) + rotar1)
        mi_sprite.do(Delay(8) + mover2)
        mi_sprite.do(Delay(10)+ mover3)
        mi_sprite.do(Delay(11)+ rotar2)
        mi_sprite.do(Delay(11.5)+ mover1)
        mi_sprite.do(Delay(11.5)+ rotar2 * 4)
        mi_sprite.do(Delay(13.5)+ MoveTo((320,240), 1))
        mi_sprite.do(Delay(13.5)+ escalar2)
        mi_sprite.do(Delay(16.5)+ Place((100,100)))

if __name__ == "__main__":
    cocos.director.director.init(caption = 'Ejemplo de accciones')
    mi_capa = MisAcciones()
    mi_escena = cocos.scene.Scene(mi_capa)
    cocos.director.director.run(mi_escena)
