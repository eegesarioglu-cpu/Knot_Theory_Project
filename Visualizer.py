import os
import webbrowser
from random import randrange
def generate_knot_svg(pd_code):
    svg_data = "<svg width='600' height='600' xmlns='http://www.w3.org/2000/svg'>\n"
    svg_data = svg_data + "<rect width='100%' height='100%' fill='#1e1e1e'/>\n"
    crossing_coords = {}
    idx = 0
    while idx < len(pd_code):
        x_pos = str(randrange(100, 500))
        y_pos = str(randrange(100, 500))
        crossing_coords[idx] = (x_pos, y_pos)
        svg_data = svg_data + "<circle cx='" + x_pos + "' cy='" + y_pos + "' r='8' fill='#ff4757'/>\n"
        label_x = str(int(x_pos) + 12)
        svg_data = svg_data + "<text x='" + label_x + "' y='" + y_pos + "' fill='white' font-family='Arial'>" + str(idx) + "</text>\n"
        idx = idx + 1
    idx = 0
    while idx < len(pd_code):
        x1 = crossing_coords[idx][0]
        y1 = crossing_coords[idx][1]
        next_idx = (idx + 1) % len(pd_code)
        x2 = crossing_coords[next_idx][0]
        y2 = crossing_coords[next_idx][1]
        svg_data = svg_data + "<line x1='" + x1 + "' y1='" + y1 + "' x2='" + x2 + "' y2='" + y2 + "' stroke='#ced6e0' stroke-width='2'/>\n"
        idx = idx + 1
    svg_data = svg_data + "</svg>"
    file_name = "temp_knot_projection.svg"
    file = open(file_name, "w")
    file.write(svg_data)
    file.close()
    absolute_path = 'file://' + os.path.realpath(file_name)
    webbrowser.open(absolute_path)
    print("\nThe knot is now displayed in your browser!")
    input("Press ENTER here in the terminal when you are done looking at it...")
    if os.path.exists(file_name):
        os.remove(file_name)
        print("Temporary visual file deleted. Workspace is clean!")
trefoil_pd = [(1, 4, 2, 5), (3, 6, 4, 1), (5, 2, 6, 3)]
generate_knot_svg(trefoil_pd)