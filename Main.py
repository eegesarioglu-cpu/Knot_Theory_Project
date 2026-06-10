import ast
import sympy as sp
from Polynomial_Math import calculate_bracket, calculate_jones_polynomial, analyze_coloring_matrix
trefoil_pd = [
    (1, 4, 2, 5),
    (3, 6, 4, 1),
    (5, 2, 6, 3)
]
trefoil_writhe = 3
hopf_link_pd = [
    (2, 4, 3, 1),
    (4, 2, 1, 3)
]
hopf_writhe = 2
def run_knot_diagnostics(name, pd_code, writhe):
    print(f"=== DIAGNOSTICS FOR: {name} ===")
    det, tricolor = analyze_coloring_matrix(pd_code)
    print(f"Knot Determinant: {det}")
    print(f"Is Tricolorable?: {tricolor}")
    bracket = calculate_bracket(pd_code)
    jones = calculate_jones_polynomial(bracket, writhe)
    print(f"Jones Polynomial: {jones}\n")
if __name__ == "__main__":
    print("Welcome to the Multi-Invariant Knot Calculator.")
    name = input("Enter the name of your knot variant: ")
    pd_string = input("Enter the PD Code as a list of tuples (e.g., [(1,4,2,5), ...]): ")
    writhe = int(input("Enter the Writhe (integer): "))
    explanation = ("\n" + 
                   "==============================================================\n" +
                   "--- A Mathematical Note on Untangling ---\n" +
                   "Why can't this program automatically untie every knot variant?\n" +
                   "\n" +
                   "In topology, there is no 'monotonic' (tekdüze) way to untie a knot.\n" +
                   "Some loops, known as 'Hard Unknots' (Zor Çözülen Düğümler), act as\n" +
                   "mathematical traps.\n" +
                   "\n" +
                   "To untangle them, you must first apply Reidemeister moves to add\n" +
                   "MORE crossings, making the knot physically larger and more complex\n" +
                   "before it can finally collapse. Because a computer cannot easily\n" +
                   "guess when to make a knot 'worse' in order to make it 'better',\n" +
                   "untangling algorithms require massive heuristic search engines or\n" +
                   "advanced Normal Surface Theory (Normal Yüzey Teorisi) rather than\n" +
                   "standard polynomials.\n" +
                   "==============================================================\n")
    print(explanation)
    try:
        user_pd_code = ast.literal_eval(pd_string)
        run_knot_diagnostics(name, user_pd_code, writhe)
    except (ValueError, SyntaxError):
        print("Error: Invalid PD Code format. Please use correct mathematical tuple syntax.")