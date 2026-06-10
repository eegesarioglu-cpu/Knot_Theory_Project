# Algorithmic Knot Theory: Jones Polynomial Calculator

This is my submission for the CENG113M Best Project Competition. It is a Python-based symbolic algebra calculator designed to compute the **Jones Polynomial** (Jones polinomu), a famous topological invariant used in mathematics and quantum physics.

## What it Does
Instead of a standard calculator, this program translates 3D continuous knot projections into discrete **Planar Diagram (PD) codes**. It then uses a graph-theory approach to compute the **Kauffman Bracket** state-sum model, adjusting for the knot's Writhe to output the exact Jones Polynomial.

## How to Run It
1. Ensure Python 3 is installed.
2. Install the required mathematical libraries:
   `pip install sympy networkx`
3. Run the execution script:
   `python3 Main.py`