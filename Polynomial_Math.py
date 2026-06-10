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
bracket_cache = {}
def calculate_bracket(crossings, current_graph=None):
    if current_graph is None:
        current_graph = nx.Graph()
    state_hash = (tuple(crossings), frozenset(current_graph.edges()))
    if state_hash in bracket_cache:
        return bracket_cache[state_hash]
    if len(crossings) == 0:
        if current_graph.number_of_nodes() == 0:
            return 1 
        loops = nx.number_connected_components(current_graph)
        result = d**(loops - 1)
        bracket_cache[state_hash] = result  
        return result
    remaining_crossings = crossings.copy()
    current_crossing = remaining_crossings.pop(0)
    arc1, arc2, arc3, arc4 = current_crossing 
    graph_A = apply_smoothing(current_graph, arc1, arc2, arc3, arc4, 'A')
    poly_A = A * calculate_bracket(remaining_crossings, graph_A) 
    
    graph_B = apply_smoothing(current_graph, arc1, arc2, arc3, arc4, 'B')
    poly_B = (A**-1) * calculate_bracket(remaining_crossings, graph_B)
    result = sp.expand(poly_A + poly_B)
    bracket_cache[state_hash] = result
    return result
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
def analyze_coloring_matrix(pd_code):
    """
    Constructs the coloring matrix from a PD code to calculate
    the Knot Determinant and check Tricolorability.
    """
    max_arc = max(max(crossing) for crossing in pd_code)
    M = sp.zeros(len(pd_code), max_arc) 
    for i, crossing in enumerate(pd_code):
        u_in, u_out, o_in, o_out = crossing
        M[i, u_in - 1] += 1
        M[i, u_out - 1] += 1
        M[i, o_in - 1] -= 1
        M[i, o_out - 1] -= 1
    minor_matrix = M[:-1, :-1]
    knot_determinant = abs(minor_matrix.det())
    is_tricolorable = (knot_determinant % 3 == 0) and (knot_determinant != 1)
    return knot_determinant, is_tricolorable
def apply_reidemeister_one_simplification(pd_code):
    """
    Scans the Planar Diagram for a Reidemeister Type I self-loop.
    If found, it mathematically removes the twist and heals the strand.
    """
    for i, crossing in enumerate(pd_code):
        if len(set(crossing)) < 4:
            edge_counts = {edge: crossing.count(edge) for edge in crossing}
            external_edges = [edge for edge, count in edge_counts.items() if count == 1]
            if len(external_edges) != 2:
                continue       
            keep_edge, remove_edge = external_edges[0], external_edges[1]
            new_pd = pd_code.copy()
            new_pd.pop(i)
            healed_pd = []
            for c in new_pd:
                healed_crossing = tuple(keep_edge if edge == remove_edge else edge for edge in c)
                healed_pd.append(healed_crossing)
            return healed_pd, True 
    return pd_code, False 
