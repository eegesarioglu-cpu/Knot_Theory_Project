import sympy as sp
import networkx as nx
A = sp.Symbol('A')
d = -A**2 - A**-2
def apply_smoothing(graph, arc1, arc2, arc3, arc4, smoothing_type):
    """
    Modifies the graph to reflect a chosen smoothing.
    A-Smoothing connects (arc1, arc2) and (arc3, arc4).
    B-Smoothing connects (arc1, arc4) and (arc2, arc3).
    """
    new_graph = graph.copy()
    if smoothing_type == 'A':
        new_graph.add_edge(arc1, arc2)
        new_graph.add_edge(arc3, arc4)
    elif smoothing_type == 'B':
        new_graph.add_edge(arc1, arc4)
        new_graph.add_edge(arc2, arc3)
    return new_graph
def calculate_bracket(crossings, current_graph=None):
    """
    Recursively calculates the Kauffman bracket state-sum.
    """
    if current_graph is None:
        current_graph = nx.Graph()
    if len(crossings) == 0:
        if current_graph.number_of_nodes() == 0:
            return 1 
        loops = nx.number_connected_components(current_graph)
        return d**(loops - 1)
    remaining_crossings = crossings.copy()
    current_crossing = remaining_crossings.pop(0)
    arc1, arc2, arc3, arc4 = current_crossing 
    graph_A = apply_smoothing(current_graph, arc1, arc2, arc3, arc4, 'A')
    poly_A = A * calculate_bracket(remaining_crossings, graph_A) 
    graph_B = apply_smoothing(current_graph, arc1, arc2, arc3, arc4, 'B')
    poly_B = (A**-1) * calculate_bracket(remaining_crossings, graph_B)
    return sp.expand(poly_A + poly_B)
def calculate_jones_polynomial(bracket, writhe):
    """
    Converts the Kauffman bracket into the Jones Polynomial 
    by adjusting for Writhe and substituting A = t^(-1/4).
    """
    normalized_bracket = ((-A**3)**-writhe) * bracket
    normalized_bracket = sp.expand(normalized_bracket)
    t = sp.Symbol('t')
    jones_poly = normalized_bracket.subs(A, t**sp.Rational(-1, 4))
    return sp.simplify(jones_poly)