# Dummy color inits
# The linter cannot find them fsr,
# so I'm defining them manually,
# they will be shadowed by the
# imported colors anyway

GREEN = 1
PURPLE = 2
BLUE = 3
ORANGE = 4
WHITE = 5
GREY = 6
YELLOW = 7
RED = 8

import copy
from manimlib.imports import *
import math

class_1_points = [
    (1,5),
    (2,2),
    (3,3), (3,5), (3,6),
    (4,1),
    (5,2), (5,6),
    (6,3), (6,5),
    (8,5),
    (9,6)
]

class_2_points = [
    (2,4),
    (2,6),
    (2,9),

    (3,7),
    (3,8),


    (4,4),
    (4,5),
    (4,6),
    (4,9),

    (5,4),
    (5,8),

    (6,7),
    (7,3),
    (7,8),

    (8,4)

]

class_3_points = [
    (5,7),

    (6,6),
    (6,8),
    (6,9),

    (7,5),
    (7,6),
    (7,7),

    (8,6),
    (8,9),
    
    (9,5),
    (9,7),
    (9,8),

    (10,5)
]


class Graphing(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "y_min": 0,
        "y_max": 10,
        "x_axis_width": 7,
        "y_axis_width": 12,
        
        "x_labeled_nums" :range(0,10,1),
        "y_labeled_nums" :range(0,10,1),
        "function_color": WHITE,
        "axes_color": BLUE,
        "x_tick_frequency": 1,
        "y_tick_frequency": 1,
        "graph_origin": 2.5 * DOWN - 6*RIGHT
    }

    def get_range_polygon(self, x_1, x_2, y_1, y_2, color=BLUE):
        return Polygon(
            self.coords_to_point(x_1, y_1), 
            self.coords_to_point(x_2, y_1), 
            self.coords_to_point(x_2, y_2), 
            self.coords_to_point(x_1, y_2), 
            n=4,
            color=color
        )

    def get_vert_line(self, x, color):
        return Polygon(
            self.coords_to_point(x, 0),
            self.coords_to_point(x, 10),
            n=2,
            color=color,
            stoke_width=0.5
        )

    def get_horz_line(self, y, color):
        return Polygon(
            self.coords_to_point(0, y),
            self.coords_to_point(10, y),
            n=2,
            color=color,
            stoke_width=0.5
        )

    def get_grid(self, sx, ex, dx, sy, ey, dy):
        def get_line(s, e):
            return Line(s, e, color=GREY, stroke_width=1)

        ctp = self.coords_to_point
        v_lines = VGroup(*[get_line(ctp(x, sy), ctp(x, ey)) for x in np.arange(sx, ex + dx, dx)])
        h_lines = VGroup(*[get_line(ctp(sx, y), ctp(ex, y)) for y in np.arange(sy, ey + dy, dy)])

        return VGroup(v_lines, h_lines)

    def draw_points(self):
        test_points = [
            ShowCreation(Dot(self.coords_to_point(*point), color=BLUE))
            for point in class_1_points
        ]

        test_points_2 = [
            ShowCreation(Dot(self.coords_to_point(*point), color=YELLOW))
            for point in class_2_points
        ]

        test_points_3 = [
            ShowCreation(Dot(self.coords_to_point(*point), color=RED))
            for point in class_3_points
        ]

        #self.play(ShowCreation(point), ShowCreation(point2))
        self.play(*test_points_3)
        self.wait(0.5)
        self.play(*test_points_2)
        self.wait(0.5)
        self.play(*test_points)
        self.wait(0.5)

    def construct(self):
        #Make graph
        self.setup_axes(animate=True)
        grid = self.get_grid(self.x_min, self.x_max, self.x_tick_frequency,
                             self.y_min, self.y_max, self.y_tick_frequency)



        rect_1 = self.get_range_polygon(1.5, 6.5, 4.5, 10.5, WHITE)
        rect_2 = self.get_range_polygon(4.5, 10.5, 6.5, 10.5, GREEN)
        rect_3 = self.get_range_polygon(4.5, 8.5, 5.5, 7.5, PURPLE)
        rect_4 = self.get_range_polygon(5.5, 10.5, 3.5, 7.5, ORANGE)
        rect_5 = self.get_range_polygon(1.5, 7.5, 0.5, 5.5)
        
        equation_1 = TextMobject(
            "$R1: A^{(1)}_{supp,1} = (1.5, 6.5), A^{2}_{supp,1} = (4.5, 10.5)$"
        )

        equation_1_1 = TextMobject(
            "$a_{1,1} = (2*2 + 4*3 + 3*4 + 3*5 + 5*6)/17 = 4.3$"
        )
        equation_1_2 = TextMobject(
            "$a_{2,1} = (3*5 + 5*6 + 3*7 + 3*8 + 3*9)/17 = 6.9$"
        )

        equation_1_1_2 = TextMobject(
            "$a_{1,1} = 4.3$"
        )
        equation_1_2_2 = TextMobject(
            "$a_{2,1} = 6.9$"
        )

        equation_2 = TextMobject(
            "$R2: A^{(1)}_{supp,2} = (4.5, 10.5), A^{2}_{supp,2} = (6.5, 10.5)$"
        )

        equation_2_1 = TextMobject(
            "$a_{1,2} = 6.8$"
        )

        equation_2_2 = TextMobject(
            "$a_{2,2} = 7.8$"
        )

        equation_3 = TextMobject(
            "$R3: A^{(1)}_{supp,3} = (4.5, 8.5), A^{2}_{supp,3} = (5.5, 7.5)$"
        )

        equation_3_1 = TextMobject(
            "$a_{1,3} = 6.3$"
        )

        equation_3_2 = TextMobject(
            "$a_{2,3} = 6.4$"
        )

        equation_4 = TextMobject(
            "$R4: A^{(1)}_{supp,4} = (5.5, 10.5), A^{2}_{supp,4} = (3.5, 7.5)$"
        )


        equation_4_1 = TextMobject(
            "$a_{1,4} = 8.1$"
        )

        equation_4_2 = TextMobject(
            "$a_{2,4} = 5.3$"
        )
 
        equation_5 = TextMobject(
            "$R5: A^{(1)}_{supp,5} = (1.5, 7.5), A^{2}_{supp,5} = (0.5, 5.5)$"
        )

        equation_5_1 = TextMobject(
            "$a_{1,5} = 4.3$"
        )

        equation_5_2 = TextMobject(
            "$a_{2,5} = 3.6$"
        )

        equation_1.set_color(WHITE)
        equation_1_1.set_color(WHITE)
        equation_1_2.set_color(WHITE)
        equation_1_1_2.set_color(WHITE)
        equation_1_2_2.set_color(WHITE)

        equation_2.set_color(GREEN)
        equation_2_1.set_color(GREEN)
        equation_2_2.set_color(GREEN)

        equation_3.set_color(PURPLE)
        equation_3_2.set_color(PURPLE)
        equation_3_1.set_color(PURPLE)

        equation_4.set_color(ORANGE)
        equation_4_1.set_color(ORANGE)
        equation_4_2.set_color(ORANGE)

        equation_5.set_color(BLUE)
        equation_5_1.set_color(BLUE)
        equation_5_2.set_color(BLUE)

        equation_1.next_to(grid, RIGHT)
        equation_1.shift(UP*2.5 - 2 * RIGHT)
        
        equation_1.scale(0.5)
        equation_1_1.scale(0.5)
        equation_1_2.scale(0.5)
        equation_1_1_2.scale(0.5)
        equation_1_2_2.scale(0.5)

        equation_2.scale(0.5)
        equation_2_1.scale(0.5)
        equation_2_2.scale(0.5)

        equation_3.scale(0.5)
        equation_3_1.scale(0.5)
        equation_3_2.scale(0.5)

        equation_4.scale(0.5)
        equation_4_1.scale(0.5)
        equation_4_2.scale(0.5)

        equation_5.scale(0.5)
        equation_5_1.scale(0.5)
        equation_5_2.scale(0.5)
        
        equation_2.next_to(equation_1, DOWN)
        equation_3.next_to(equation_2, DOWN)
        equation_4.next_to(equation_3, DOWN)
        equation_5.next_to(equation_4, DOWN)


        equation_1_1.next_to(equation_1, DOWN)
        equation_1_1_2.next_to(equation_1, DOWN)
        equation_1_2.next_to(equation_1_1, DOWN)
        equation_1_2_2.next_to(equation_1_1, DOWN)

        equation_2_1.next_to(equation_1_2, DOWN)
        equation_2_2.next_to(equation_2_1, DOWN)

        equation_3_1.next_to(equation_2_2, DOWN)
        equation_3_2.next_to(equation_3_1, DOWN)

        equation_4_1.next_to(equation_3_2, DOWN)
        equation_4_2.next_to(equation_4_1, DOWN)

        equation_5_1.next_to(equation_4_2, DOWN)
        equation_5_2.next_to(equation_5_1, DOWN)


        #Display graph
        self.play( ShowCreation(grid))
        self.wait(1)

        self.draw_points()

        self.play(ShowCreation(rect_1), ShowCreation(equation_1))
        self.wait(1)


        self.play(ShowCreation(rect_2), ShowCreation(equation_2))
        self.wait(1)


        self.play(ShowCreation(rect_3), ShowCreation(equation_3))
        self.wait(1)


        self.play(ShowCreation(rect_4), ShowCreation(equation_4))
        self.wait(1)


        self.play(ShowCreation(rect_5), ShowCreation(equation_5))
        self.wait(1)


        self.wait(1)

        eq1_1_line = self.get_vert_line(4.3, WHITE)
        eq1_2_line = self.get_horz_line(6.9, WHITE)

        self.play(
            FadeOut(rect_2),
            FadeOut(rect_3),
            FadeOut(rect_4),
            FadeOut(rect_5),
            FadeOut(equation_2),
            FadeOut(equation_3),
            FadeOut(equation_4),
            FadeOut(equation_5),

            FadeIn(equation_1_1),
            FadeIn(equation_1_2),
        )
        self.wait(1)

        dots_col_2 = [
            Dot(self.coords_to_point(2, 6), color=YELLOW, radius=0.15),
            Dot(self.coords_to_point(2, 9), color=YELLOW, radius=0.15)
        ]


        self.play(
            *[
                GrowFromCenter(dot) for dot in dots_col_2
            ]
        )

        self.wait(2)


        self.play(
            *[
                ShrinkToCenter(dot) for dot in dots_col_2
            ]
        )

        dots_col_3 = [
            Dot(self.coords_to_point(3, 5), color=BLUE, radius=0.15),
            Dot(self.coords_to_point(3, 6), color=BLUE, radius=0.15),
            Dot(self.coords_to_point(3, 7), color=YELLOW, radius=0.15),
            Dot(self.coords_to_point(3, 8), color=YELLOW, radius=0.15)
        ]

        self.play(
            *[
                GrowFromCenter(dot) for dot in dots_col_3
            ]
        )

        self.wait(2)

        self.play(
            *[
                ShrinkToCenter(dot) for dot in dots_col_3
            ]
        )

        # return

        self.play(
            ReplacementTransform(equation_1_1, equation_1_1_2),
            ReplacementTransform(equation_1_2, equation_1_2_2),
        )

        self.wait(1)

        self.play(
            FadeIn(eq1_1_line),
            FadeIn(eq1_2_line)
        )

        self.wait(1)


        self.play(
            FadeOut(eq1_1_line),
            FadeOut(eq1_2_line)
        )
        self.wait(1)

        self.play(
            FadeOut(equation_1),
            FadeOut(rect_1)
        )

        eq2_1_line = self.get_vert_line(6.8, GREEN)
        eq2_2_line = self.get_horz_line(7.8, GREEN)


        self.wait(0.5)


        self.play(
            FadeIn(equation_2_1),
            FadeIn(equation_2_2),
            FadeIn(rect_2),
            FadeIn(eq2_1_line),
            FadeIn(eq2_2_line)
        )

        self.wait(1)

        eq3_1_line = self.get_vert_line(6.3, PURPLE)
        eq3_2_line = self.get_horz_line(6.4, PURPLE)

        self.play(
            FadeOut(rect_2),
            FadeOut(eq2_1_line),
            FadeOut(eq2_2_line),
            FadeIn(equation_3_1),
            FadeIn(equation_3_2),
            FadeIn(rect_3),
            FadeIn(eq3_1_line),
            FadeIn(eq3_2_line)
        )
        self.wait(1)

        eq4_1_line = self.get_vert_line(8.1, ORANGE)
        eq4_2_line = self.get_horz_line(5.3, ORANGE)

        self.play(
            FadeOut(rect_3),
            FadeOut(eq3_1_line),
            FadeOut(eq3_2_line),
            FadeIn(equation_4_1),
            FadeIn(equation_4_2),
            FadeIn(rect_4),
            FadeIn(eq4_1_line),
            FadeIn(eq4_2_line)
        )

        self.wait(1)

        eq5_1_line = self.get_vert_line(4.3, BLUE)
        eq5_2_line = self.get_horz_line(3.6, BLUE)

        self.play(
            FadeOut(rect_4),
            FadeOut(eq4_1_line),
            FadeOut(eq4_2_line),
            FadeIn(equation_5_1),
            FadeIn(equation_5_2),
            FadeIn(rect_5),
            FadeIn(eq5_1_line),
            FadeIn(eq5_2_line)
        )

        self.wait(2)

        self.play(
            FadeOut(rect_5),
            FadeOut(eq5_1_line),
            FadeOut(eq5_2_line),
        )

        self.wait(2)

        r1_1 = TextMobject("$R1: (1.5, 4.3, 6.5)_T$ $I(4.5, 6.9, 10.5)_T $ →")
        r1_2 = TextMobject("→ ${(1, 0.24), (2, 0.53), (3, 0.25)}$")

        r1_1.next_to(equation_1, DOWN)
        r1_1.shift(UP)
        r1_2.next_to(r1_1, DOWN)
        r1_2.shift(UP * 0.3)

        r1_1.scale(0.5)
        r1_2.scale(0.5)

        self.play(
            ReplacementTransform(equation_1_1_2, r1_1),
            ReplacementTransform(equation_1_2_2, r1_2),
            ShowCreation(rect_1)
        )

        self.wait(3)

        r2_1 = TextMobject("$R2: (4.5, 6.8, 10.5)_T$ $I(6.5, 7.8, 10.5)_T$ →")
        r2_2 = TextMobject("→ ${(1, 0), (2, 0.3), (3, 0.7)}$")

        r2_1.scale(0.5)
        r2_2.scale(0.5)

        r2_1.set_color(GREEN)
        r2_2.set_color(GREEN) 


        r2_1.next_to(r1_2, DOWN)
        # r2_2.shift(DOWN)
        r2_2.next_to(r2_1, DOWN)

        self.play(
            FadeOut(rect_1),
            ReplacementTransform(equation_2_1, r2_1),
            ReplacementTransform(equation_2_2, r2_2),
            ShowCreation(rect_2)
        )

        self.wait(3)

        r3_1 = TextMobject("$R3: (4.5, 6.3, 8.5)_T$ $I(5.5, 6.4, 7.5)_T$ →")
        r3_2 = TextMobject("→ ${(1, 0.14), (2, 0.14), (3, 0.71)}$")

        r3_1.scale(0.5)
        r3_2.scale(0.5)

        r3_1.set_color(PURPLE)
        r3_2.set_color(PURPLE) 


        r3_1.next_to(r2_2, DOWN)
        # r2_2.shift(DOWN)
        r3_2.next_to(r3_1, DOWN)

        self.play(
            FadeOut(rect_2),
            ReplacementTransform(equation_3_1, r3_1),
            ReplacementTransform(equation_3_2, r3_2),
            ShowCreation(rect_3)
        )

        self.wait(3)

        r4_1 = TextMobject("$R4: (5.5, 8.1, 10.5)_T$ $I(3.5, 5.3, 7.5)_T$ →")
        r4_2 = TextMobject("→ ${(1, 0.23), (2, 0.077), (3, 0.69)}$")

        r4_1.scale(0.5)
        r4_2.scale(0.5)

        r4_1.set_color(ORANGE)
        r4_2.set_color(ORANGE) 

        r4_1.next_to(r3_2, DOWN)
        # r2_2.shift(DOWN)
        r4_2.next_to(r4_1, DOWN)

        self.play(
            FadeOut(rect_3),
            ReplacementTransform(equation_4_1, r4_1),
            ReplacementTransform(equation_4_2, r4_2),
            ShowCreation(rect_4)
        )

        self.wait(3)

        r5_1 = TextMobject("$R5: (1.5, 4.3, 7.5)_T$ $I(0.5, 3.6, 5.5)_T$ →")
        r5_2 = TextMobject("→ ${(1, 0.69), (2, 0.15), (3, 0.15)}$")

        r5_1.scale(0.5)
        r5_2.scale(0.5)

        r5_1.set_color(BLUE)
        r5_2.set_color(BLUE) 

        r5_1.next_to(r4_2, DOWN)
        # r2_2.shift(DOWN)
        r5_2.next_to(r5_1, DOWN)

        self.play(
            FadeOut(rect_4),
            ReplacementTransform(equation_5_1, r5_1),
            ReplacementTransform(equation_5_2, r5_2),
            ShowCreation(rect_5)
        )

        self.wait(3)

        self.play(
            FadeOut(rect_5)

        )

        self.wait(2)

        dot_to_calculate = Dot(self.coords_to_point(6, 6), color=WHITE, radius=0.15)

        self.play(
            GrowFromCenter(dot_to_calculate),
            FocusOn(dot_to_calculate)
        )

        self.wait(1)

        self.play(
            ShowCreation(rect_1),  
            ShowCreation(rect_2),  
            ShowCreation(rect_3),  
            ShowCreation(rect_4),
            ShowCreation(rect_5)
        )


        self.wait(1)
        self.play(
            FadeOut(rect_2)
        )

        self.wait(2)

        self.play(
            FadeOut(rect_5)
        )

        self.wait(2)

        self.play(
            FadeOut(r2_1),  
            FadeOut(r2_2)
        )

        self.play(
            FadeOut(r5_1),  
            FadeOut(r5_2)
        )


        self.wait(2)


        r4_1_old = r4_1
        r4_2_old = r4_2

        r4_1 = copy.deepcopy(r4_1_old)
        r4_2 = copy.deepcopy(r4_2_old)

        r4_1.shift(DOWN)
        r4_2.shift(DOWN)

        self.play(
            ReplacementTransform(r4_1_old, r4_1),
            ReplacementTransform(r4_2_old, r4_2),
        )


        self.wait(3)

        fuzzy_activation_function = ImageMobject('fuzzy_activation_function.png')
        fuzzy_activation_function.stretch_in_place(0.8, 0)
        fuzzy_activation_function.stretch_in_place(0.8, 1)
        fuzzy_activation_function.move_to(r4_2, DOWN)
        fuzzy_activation_function.shift(DOWN * 2.4)

        self.play(
            FadeIn(fuzzy_activation_function)
        )

        self.wait(2)

        r1_activation = TextMobject("$v_1(\overline{x}) = min\{ 0.23, 0.62 \} = 0.23 $")
        r1_activation.scale(0.5)
        r1_activation.next_to(r1_2, DOWN)

        self.play(
            ShowCreation(r1_activation)
        )

        self.wait(2)

        r3_activation = TextMobject("$v_3(\overline{x}) = min\{ 0.83, 0.56 \} = 0.56 $")
        r3_activation.scale(0.5)
        r3_activation.set_color(PURPLE)
        r3_activation.next_to(r3_2, DOWN)

        self.play(
            ShowCreation(r3_activation)
        )

        self.wait(2)

        r4_activation = TextMobject("$v_4(\overline{x}) = min\{ 0.19, 0.68 \} = 0.19 $")
        r4_activation.scale(0.5)
        r4_activation.set_color(ORANGE)
        r4_activation.next_to(r4_2, DOWN)

        self.play(
            ShowCreation(r4_activation)
        )

        self.wait(2)
        self.play(
            FadeOut(fuzzy_activation_function),
            FadeOut(rect_3),
            FadeOut(rect_4)
        )

        self.wait(2)
        r1_conclusion_1 = TextMobject("$B_1(\overline{x}) = \{ (1, 0.24 * 0.23), (2, 0.53 * 0.23), (3, 0.25 * 0.23) \}$")
        r1_conclusion_2 = TextMobject("$B_1(\overline{x}) = \{ (1, 0.055), (2, 0.12), (3, 0.58) \}$")

        r1_conclusion_1.scale(0.5)
        r1_conclusion_2.scale(0.5)
        
        r1_conclusion_1.next_to(r1_activation, DOWN)
        r1_conclusion_2.next_to(r1_activation, DOWN)
            
        self.play(ShowCreation(r1_conclusion_1))
        self.wait(3)
        self.play(ReplacementTransform(r1_conclusion_1, r1_conclusion_2))
        
        self.wait(2)


        r3_conclusion_1 = TextMobject("$B_3(\overline{x}) = \{ (1, 0.14 * 0.56), (2, 0.14 * 0.56), (3, 0.71 * 0.56) \}$")
        r3_conclusion_2 = TextMobject("$B_3(\overline{x}) = \{ (1, 0.055), (2, 0.12), (3, 0.58) \}$")

        r3_conclusion_1.scale(0.5)
        r3_conclusion_2.scale(0.5)
        
        r3_conclusion_1.next_to(r3_activation, DOWN)
        r3_conclusion_2.next_to(r3_activation, DOWN)
        
        r3_conclusion_1.set_color(PURPLE)
        r3_conclusion_2.set_color(PURPLE)

            
        self.play(ShowCreation(rect_3))
        self.play(ShowCreation(r3_conclusion_1))
        self.wait(3)
        self.play(ReplacementTransform(r3_conclusion_1, r3_conclusion_2))
        
        self.wait(2)
        r4_conclusion_1 = TextMobject("$B_4(\overline{x}) = \{ (1, 0.23 * 0.19), (2, 0.077 * 0.19), (3, 0.69 * 0.19) \}$")
        # ${(1, 0.23), (2, 0.077), (3, 0.69)}$")
        r4_conclusion_2 = TextMobject("$B_4(\overline{x}) = \{ (1, 0.044), (2, 0.15), (3, 0.13) \}$")
        r4_conclusion_2.set_color(ORANGE)

        r4_conclusion_1.scale(0.5)
        r4_conclusion_2.scale(0.5)
        
        r4_conclusion_1.next_to(r4_activation, DOWN)
        r4_conclusion_2.next_to(r4_activation, DOWN)
            
        self.play(ShowCreation(rect_4))
        self.play(ShowCreation(r4_conclusion_2))
        

        self.wait(3)

        result_1 = TextMobject("$B(\overline{x}) = \{(1, 0.055), (2, 0.15), (3, 0.58)\}$")
        result_2 = TextMobject("$B(\overline{x}) = \{(1, 0.055), (2, 0.15), (3, 0.58)\}$")
        result_3 = TextMobject("$B\overline{y}(\overline{x}) = 3$")

        result_1.scale(0.5)
        result_2.scale(0.5)

        result_1.next_to(r4_conclusion_2, DOWN*1.1)
        result_2.next_to(r4_conclusion_2, DOWN*1.1)
        result_3.next_to(result_2, DOWN)

        result_2.set_color(YELLOW)
        result_3.set_color(YELLOW)

        self.play(ShowCreation(result_1))
        self.wait(1)

        self.play(ShowCreation(result_3))
        self.wait(1)

        dot_to_calculate_yellow = Dot(self.coords_to_point(6, 6), color=YELLOW, radius=0.15)


        self.play(
            FocusOn(dot_to_calculate)
        )

        self.play(
            GrowFromCenter(dot_to_calculate_yellow)
        )

        self.play(
            Indicate(dot_to_calculate_yellow)
        )


        self.wait(5)
        return

