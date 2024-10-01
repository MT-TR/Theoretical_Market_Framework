from graphviz import Digraph

def create_graphical_tree(elements, elements_names, filename='output_tree', dpi=300):
    """
    Creates a graphical tree with custom color palette, bold font for the root using a relative font path, and a vertically oriented legend.
    
    :param elements: dict, tree structure with parent-child relationships
    :param filename: str, name of the file to save the output
    :param dpi: int, resolution for the output
    """
    dot = Digraph(comment="Element Tree")
    # Define default node shape as square (box)
    #dot.attr('node', shape='box'
    #dot.attr('node', shape='box', width='1', height='1'))
    dot.attr('node', shape='box', style='filled', color='black', width='1', height='1', fontname='Calibri', fontsize='12', fontcolor='black')
    # Set default edge attributes to remove arrows
    dot.attr('edge', arrowhead='none')
    # Set horizontal layout (left to right)
    # dot.attr(rankdir='LR') # dot.attr(rankdir='TB') # top to bottom
    # Add a title to the main tree using the graph's label
    dot.attr(label=filename, labelloc="t", fontsize="24", fontname='Calibri')  # Title at the top, with larger font

     # Custom color palette
    colors = {
        0: {'fillcolor': '#001f3f', 'fontcolor': 'white', 'fontname': 'Calibri'},  # Root: Dark blue, white font
        1: {'fillcolor': '#0074D9', 'fontcolor': 'white', 'fontname': 'Calibri'},  # Child: Blue, white font
        2: {'fillcolor': '#7FDBFF', 'fontcolor': 'black', 'fontname': 'Calibri'},  # Sub-child: Light blue, black font
        3: {'fillcolor': '#DDDDDD', 'fontcolor': 'black', 'fontname': 'Calibri'}   # Sub-sub-child: Light gray, black font
    }


    # Recursive function to add nodes with the same color per level
    def add_nodes_and_edges(parent, children, level):
        # Add the parent node with the color and font style for the current level
        dot.node(parent, parent, fillcolor=colors[level]['fillcolor'], fontcolor=colors[level]['fontcolor'], fontname=colors[level]['fontname'])
        
        # Add child nodes and edges
        for child in children:
            # Determine if the child has its own children
            if child in elements:
                # Recursively add sub-children with the next level's color
                add_nodes_and_edges(child, elements_names[child], level + 1)
            else:
                # Add sub-child node with the next level's color and font
                dot.node(child, elements_names[child], fillcolor=colors[level + 1]['fillcolor'], fontcolor=colors[level + 1]['fontcolor'], fontname=colors[level + 1]['fontname'])
            
            # Create the edge (relationship between parent and child) without arrows
            dot.edge(parent, child)

    # Start the tree with the root node at level 0
    root = "Root"
    add_nodes_and_edges(root, elements[root], level=0)
    
    
    # Create a separate legend under the invisible root
    with dot.subgraph(name='cluster_legend') as legend:
        legend.attr(label="Legend", fontsize="20", style="solid", rankdir="TB")
        
        # Add legend nodes (not part of the main plot)
        legend.node("Legend_Root", "Root", fillcolor=colors[0]['fillcolor'], fontcolor=colors[0]['fontcolor'], fontname=colors[0]['fontname'])
        legend.node("Legend_Child", "Child", fillcolor=colors[1]['fillcolor'], fontcolor=colors[1]['fontcolor'], fontname=colors[1]['fontname'])
        legend.node("Legend_SubChild", "Sub-child", fillcolor=colors[2]['fillcolor'], fontcolor=colors[2]['fontcolor'], fontname=colors[2]['fontname'])
        legend.node("Legend_SubSubChild", "Sub-sub-child", fillcolor=colors[3]['fillcolor'], fontcolor=colors[3]['fontcolor'], fontname=colors[3]['fontname'])

        # Vertical layout for the legend
        legend.edge("Legend_Root", "Legend_Child", style="invis")
        legend.edge("Legend_Child", "Legend_SubChild", style="invis")
        legend.edge("Legend_SubChild", "Legend_SubSubChild", style="invis")

    # Add an invisible spacer node to increase horizontal space and position legend to the right
    # dot.node("Spacer", style="invis", width="2")  # The width of "Spacer" determines horizontal space
    # dot.edge(root, "Spacer", style="invis")       # Connect tree to spacer invisibly
    
    # Position the legend to the right of the spacer
    # dot.edge("Spacer", "Legend_Root", style="invis")  # Connect spacer to the legend invisibly


    # Set the DPI for higher image quality
    #dot.attr(dpi=str(dpi)) # valid only if format is 'svg'
    # Render the tree to an SVG file
    output_filename = f"{filename}"
    dot.render(output_filename, format='svg')
    print(f"Graphical tree generated and saved as '{output_filename}'")
