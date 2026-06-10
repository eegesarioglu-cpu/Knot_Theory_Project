
import sympy as sp
from Polynomial_Math import calculate_bracket, calculate_jones_polynomial
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
print("=== HOPF LINK ===")
hopf_bracket = calculate_bracket(hopf_link_pd)
hopf_jones = calculate_jones_polynomial(hopf_bracket, hopf_writhe)
print(f"Kauffman Bracket: {hopf_bracket}")
print(f"Jones Polynomial: {hopf_jones}\n")
print("=== TREFOIL KNOT ===")
trefoil_bracket = calculate_bracket(trefoil_pd)
trefoil_jones = calculate_jones_polynomial(trefoil_bracket, trefoil_writhe)
print(f"Kauffman Bracket: {trefoil_bracket}")
print(f"Jones Polynomial: {trefoil_jones}")
left_trefoil_pd = [
    (4, 1, 5, 2),
    (6, 3, 1, 4),
    (2, 5, 3, 6)
]
left_trefoil_writhe = -3
print("=== LEFT-HANDED TREFOIL ===")
left_bracket = calculate_bracket(left_trefoil_pd)
left_jones = calculate_jones_polynomial(left_bracket, left_trefoil_writhe)
print(f"Jones Polynomial: {left_jones}")