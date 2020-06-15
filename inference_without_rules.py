from manimlib.imports import *

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


from manimlib.imports import *

colors = [ RED, BLUE, PURPLE, ORANGE, YELLOW, BLUE, GREEN, WHITE]
import math


class GetMinMax(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": 0,
        "y_max": 1,
        "x_axis_width": 10,
        "y_axis_height": 0,
        
        # "x_labeled_nums" :range(0,10,1),
        # "y_labeled_nums" :range(0,10,1),
        "function_color": WHITE,
        "axes_color": BLUE,
        "x_tick_frequency": 1,
        "y_tick_frequency": 1,
        "graph_origin": - 0.9*RIGHT,
        "y_axis_label": "",
    }


    def construct(self):
        # Make graph
        self.setup_axes(animate=True)
        
        self.wait(2)

        dot_1 = Dot(self.coords_to_point(-5, 0))
        dot_2 = Dot(self.coords_to_point(-4, 0))
        dot_3 = Dot(self.coords_to_point(-2, 0))
        dot_4 = Dot(self.coords_to_point(-1, 0))
        dot_5 = Dot(self.coords_to_point(1, 0))
        dot_6 = Dot(self.coords_to_point(2, 0))
        dot_7 = Dot(self.coords_to_point(3, 0))
        dot_8 = Dot(self.coords_to_point(5, 0))

        self.play(ShowCreation(dot_1))
        self.play(ShowCreation(dot_2))
        self.play(ShowCreation(dot_3))
        self.play(ShowCreation(dot_4))
        self.play(ShowCreation(dot_6))
        self.play(ShowCreation(dot_7))
        self.play(ShowCreation(dot_8))

        dot_min = Dot(self.coords_to_point(-5, 0))
        dot_max = Dot(self.coords_to_point(5, 0))

        self.wait(2)
        
        text_min = TextMobject("$x_{min}$")
        text_max = TextMobject("$x_{max}$")

        text_min.next_to(dot_min, DOWN)
        text_max.next_to(dot_max, DOWN)

        self.play(Indicate(dot_1), ShowCreation(text_min))
        self.wait(1)
        self.play(Indicate(dot_8), ShowCreation(text_max))

        self.wait(4)
        

class HowManyDivisions(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": 0,
        "y_max": 1,
        "x_axis_width": 10,
        "y_axis_height": 3,
        
        # "x_labeled_nums" :range(0,10,1),
        # "y_labeled_nums" :range(0,10,1),
        "function_color": WHITE,
        "axes_color": BLUE,
        "x_tick_frequency": 1,
        "y_tick_frequency": 1,
        "graph_origin": 2.5 * DOWN - 1*RIGHT
    }

    def get_fuzzy_number(self, min, top, max, color=BLUE):
        point_min = self.coords_to_point(min, 0)
        point_top = self.coords_to_point(top, 1)
        point_max = self.coords_to_point(max, 0)

        return Line(point_min, point_top, color=color), Line(point_top, point_max, color=color)


    def get_range_polygon(self, x_1, x_2, y_1, y_2, color=BLUE):
        return Polygon(
            self.coords_to_point(x_1, y_1), 
            self.coords_to_point(x_2, y_1), 
            self.coords_to_point(x_2, y_2), 
            self.coords_to_point(x_1, y_2), 
            n=4,
            color=color
        )

    def get_grid(self, sx, ex, dx, sy, ey, dy):
        def get_line(s, e):
            return Line(s, e, color=GREY, stroke_width=1)

        ctp = self.coords_to_point
        v_lines = VGroup(*[get_line(ctp(x, sy), ctp(x, ey)) for x in np.arange(sx, ex + dx, dx)])
        h_lines = VGroup(*[get_line(ctp(sx, y), ctp(ex, y)) for y in np.arange(sy, ey + dy, dy)])

        return VGroup(v_lines, h_lines)

    def construct(self):
        # Make graph
        self.setup_axes(animate=True)
        
        self.wait(2)

        colors = [ RED, BLUE, PURPLE, ORANGE, YELLOW, BLUE, GREEN, WHITE]

        dot_min = Dot(self.coords_to_point(-3, 0))
        dot_max = Dot(self.coords_to_point(3, 0))
        
        text_min = TextMobject("$x_{min}$")
        text_max = TextMobject("$x_{max}$")

        text_min.next_to(dot_min, DOWN)
        text_max.next_to(dot_max, DOWN)

        self.play(ShowCreation(dot_min), ShowCreation(text_min))
        self.wait(1)
        self.play(ShowCreation(dot_max), ShowCreation(text_max))
        

        self.wait(2)

        lines = []
        for i in range(-5, 3, 2):
            l1, l2 = self.get_fuzzy_number(i,i+2,i+4, color=colors[(i+5) % 8])
            self.play(ShowCreation(l1)) 
            self.play(ShowCreation(l2))
            lines.append(l1)
            lines.append(l2)

        self.wait(1)
        self.play( *[FadeOut(line) for line in lines] )

        lines = []
        for i in range(-4, 3, 1):
            l1, l2 = self.get_fuzzy_number(i,i+1,i+2, color=colors[(i+5) % 8])
            self.play(ShowCreation(l1)) 
            self.play(ShowCreation(l2))
            lines.append(l1)
            lines.append(l2)

        self.wait(2)
        ##self.play( *[FadeOut(line) for line in lines] )

        num_of_cechy = TextMobject('$k$ - liczba cech, $L_i$ - liczba zbiorów pokrywających $i$-tą cechę')
        num_of_cechy.scale(0.6)
        num_of_cechy.shift(UP * 3)
        
        l_1 = TextMobject('$L_1$')

        l_1.shift(LEFT * 6 + UP * 2)
        l_2 = TextMobject('$*$ $L_2$')
        l_3 = TextMobject('$*$ $L_3$ $*$ $...$ * $L_k$')
        l_2.next_to(l_1, RIGHT)
        l_3.next_to(l_2, RIGHT)

        self.play(ShowCreation(num_of_cechy))
        self.wait(4)
        self.play(ShowCreation(l_1))
        self.wait(3)
        self.play(ShowCreation(l_2))
        self.wait(2)
        self.play(ShowCreation(l_3))
        self.wait(2)

        less_than = TextMobject('$< N $ ← Liczba obiektów uczących')
        less_than.next_to(l_3, RIGHT)
        self.play(ShowCreation(less_than))

        self.wait(3)        



class HowManyRules(GraphScene):
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

   
    def get_grid(self, sx, ex, dx, sy, ey, dy):
        def get_line(s, e):
            return Line(s, e, color=GREY, stroke_width=1)

        ctp = self.coords_to_point
        v_lines = VGroup(*[get_line(ctp(x, sy), ctp(x, ey)) for x in np.arange(sx, ex + dx, dx)])
        h_lines = VGroup(*[get_line(ctp(sx, y), ctp(ex, y)) for y in np.arange(sy, ey + dy, dy)])

        return VGroup(v_lines, h_lines)

    def construct(self):
        #Make graph
        self.setup_axes(animate=True)
        grid = self.get_grid(self.x_min, self.x_max, self.x_tick_frequency,
                             self.y_min, self.y_max, self.y_tick_frequency)


        self.play(ShowCreation(grid))

        self.wait(1)

        points_raw = [
            (3, 2),
            (1, 4),
            (5, 3),
            (6, 1),
            (7, 3),
            (3, 8),
            (8, 8),
            (7, 6),
        ]

        points = [
            self.coords_to_point(*point)
            for point in points_raw
        ]


        dots = []
        counter = 0
        for point in points:
            dots.append(Dot(point, color=colors[counter], radius=0.12))
            dots.append(Dot(point, color=colors[counter], radius=0.12))
            counter += 1
        

        self.play(
            *[
                ShowCreation(dot) for dot in dots
            ]
        )

        self.wait(1)
        
        height = 0

        lol = False
        for dot in dots:
            lol = not lol
            if lol == False:
                continue

            height += 1
            
            text = TextMobject(f'$R_{height}$')
            text.next_to(grid, RIGHT)
            text.shift(DOWN * (height-4) + RIGHT)
            text.set_color(dot.color)
            self.play(ReplacementTransform(dot, text))
            self.wait(0.5)
