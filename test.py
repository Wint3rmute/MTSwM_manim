from manimlib.imports import *
import math

class Graphing(DiscreteGraphScene):
    CONFIG = {
        "x_axis_label": "x",
        "y_axis_label": "$\mu$",
        "x_min": 0,
        "x_max": 1,
        "y_min": 0,
        "y_max": 1,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE,
        "graph_origin": 3 * DOWN + 4 * LEFT
    }

    def construct(self):
        #Make graph
        self.setup_axes(animate=True)
        func_graph= self.get_graph(self.func_to_graph,self.function_color)
        graph_lab = self.get_graph_label(func_graph, label = "x^{2}")

        func_graph_2=self.get_graph(self.func_to_graph_2,self.function_color)
        graph_lab_2 = self.get_graph_label(func_graph_2, label = "x^{3}")

        vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)

        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))
        horz_line = Line(x,y, color=YELLOW)

        point = Dot(self.coords_to_point(1,self.func_to_graph(1)))

        #Display graph
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(1)
        self.play(ShowCreation(vert_line))
        self.play(ShowCreation(horz_line))
        self.add(point)
        self.wait(1)
        self.play(Transform(func_graph, func_graph_2), Transform(graph_lab, graph_lab_2))
        self.wait(2)


    def func_to_graph(self, x):
        if x < 0.2:
            return 0
        if x == 0.4:
            return 1
        return None

    def func_to_graph_2(self, x):
        return(x**3)