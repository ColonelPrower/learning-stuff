import cocos
from cocos.scenes.transitions import FadeTransition

Clayer = cocos.layer
Ctext = cocos.text
Cdirector = cocos.director
Cscene = cocos.scene

class VerTexto(Clayer.Layer):
    def __init__(self):
        super().__init__()
        mi_etiqueta = Ctext.Label(
            'Escena 1',
            font_name = 'Consolas',
            font_size= 18,
            anchor_x = 'center',
            anchor_y = 'center',
        )
        mi_etiqueta.position = (320,240)
        self.add(mi_etiqueta)

class VerTexto2(Clayer.Layer):
    def __init__(self):
        super().__init__()
        mi_etiqueta = Ctext.Label(
            'Escena 2',
            font_name = 'Consolas',
            font_size = 18,
            anchor_x = 'center',
            anchor_y = 'center'
        )
        mi_etiqueta.position = (320,240)
        self.add(mi_etiqueta)

if __name__ == "__main__":
    Cdirector.director.init(caption = "Sencilla transcicion entre escenas")
    escena_1 = Cscene.Scene(VerTexto())
    escena_2 = Cscene.Scene(VerTexto2())
    Cdirector.director.run(FadeTransition(escena_2,5,escena_1))
    