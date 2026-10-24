
import networkx as nx


class Graph:
    def __init__(self, orientovany=False):
        self.graf = nx.DiGraph() if orientovany else nx.Graph()

    def pridej_uzel(self, uzel):
        self.graf.add_node(uzel)

    def pridej_hranu(self, a, b, vaha=None):
        self.graf.add_edge(a, b, vaha=vaha)

    def smaz_uzel(self, uzel):
        self.graf.remove_node(uzel)

    def smaz_hranu(self, a, b):
        self.graf.remove_edge(a, b)

    def analyze(self):
        g = self.graf

        print("Počet uzlů:", g.number_of_nodes())
        print("Počet hran:", g.number_of_edges())
        print("Orientovaný:", g.is_directed())
        print("Ohodnocený:", any(
            "vaha" in data and data["vaha"] is not None
            for _, _, data in g.edges(data=True)
        ))
        print("Obsahuje smyčky:", nx.number_of_selfloops(g) > 0)

        jednoduchy = nx.Graph(g)
        print("Planární:", nx.check_planarity(jednoduchy)[0])

        if nx.number_of_selfloops(g) > 0:
            print("Chromatické číslo: nelze určit")
        else:
            barvy = nx.coloring.greedy_color(jednoduchy)
            print("Chromatické číslo (horní odhad):",
                  max(barvy.values(), default=-1) + 1)

