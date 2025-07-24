import cocos
from cocos.actions import *
from cocos.layer import * 
from cocos.sprite import *

class MisAcciones(ColorLayer):
    def __init__(self):
        super().__init__(64,200,255,255)

        mi_sprite = Sprite('mi_guerrero.png')
        mi_sprite.position = 590,240
        mi_sprite.scale = 1.5
        self.add(mi_sprite)

        mi_sprite.do(CallFuncS(lambda obj: self.discontinuo(
            obj,5,(-100,0),1
        )))
        mi_sprite.do(Delay(6)+CallFuncS(lambda obj: self.mover_girando(
            obj,(550,80),3,3
        )))
        mi_sprite.do(Delay(9)+AccelDeccel(MoveBy((0,350),3)|RotateBy(360,3)))
        mi_sprite.do(Delay(12)+Accelerate(MoveBy((-450,0),3)|RotateBy(360,3)),4)
        mi_sprite.do(Delay(16)+(MoveBy((0,-400),3)|FadeOut(3)))
    
    def discontinuo(self,obj,n_pasos,vector,tiempo):
        pass
    