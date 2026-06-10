# Algorithmic Knot Theory: Multi-Invariant Calculator

This is my submission for the CENG113M Best Project Competition. It is an interactive Python-based computational topology engine designed to rigorously compute a suite of topological invariants, including the **Jones Polynomial** (Jones polinomu), the **Knot Determinant** (Düğüm determinantı), and **Tricolorability** (Üç renklendirilebilirlik).

## What it Does
Instead of a standard mathematical calculator, this program translates 3D continuous knot projections into discrete **Planar Diagram (PD) codes** and runs them through a multi-layered diagnostic filter:
1. **Linear Algebra:** It constructs a coloring matrix from the PD code to calculate the determinant and prove $p$-colorability.
2. **Graph Theory & Dynamic Programming:** It maps topological states to undirected graphs, utilizing a memory cache to collapse the exponential $O(2^n)$ complexity of the **Kauffman Bracket** state-sum model.
3. **Symbolic Algebra:** It adjusts for the knot's Writhe to output the exact Jones Polynomial using pure algebraic variables.

## How to Run It
1. Ensure Python 3 is installed.
2. Install the required mathematical libraries:
   `pip install -r requirements.txt`
3. Run the interactive execution script:
   `python3 Main.py`
4. Follow the terminal prompts to safely input your knot's PD array and Writhe.