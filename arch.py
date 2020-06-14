from manimlib.imports import *


class Scena(Scene):
    def construct(self):
        logo = SVGMobject('arch.svg')
        logo.scale(2)

        text_arch = TextMobject(
            "Arch"
        )


        shift = 0.215
        text_arch.set_color(BLUE)
        text_arch.shift(RIGHT * shift)


        text_arch2 = TextMobject(
            "Arch"
        )

        text_arch2.set_color(BLUE)
        text_arch2.shift(RIGHT * shift)


        text = TextMobject(
            "I use Arch btw"
        )

        text.scale(2)
        text_arch.scale(2)
        text_arch2.scale(2)

        self.play(FadeIn(logo))
        self.wait(1)
        
        self.play(
                ReplacementTransform(logo, text_arch)
                
        )
        
        self.play(
                FadeIn(text),                
                FadeIn(text_arch2)
        )

        self.wait(1)

        self.play(
                FadeOut(text),
                FadeOut(text_arch2),
                FadeOut(text_arch)
                )
        self.wait(1)
