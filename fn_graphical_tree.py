from graphviz import Digraph

def create_graphical_tree(elements, elements_names, filename='output_tree', dpi=300):
    """
    Creates a graphical tree with custom color palette and support for displaying custom labels
    and allowing parents to have subchildren without children.
    
    :param elements: dict, tree structure with parent-child relationships
    :param elements_names: dict, dictionary mapping node internal names to display names
    :param filename: str, name of the file to save the output
    :param dpi: int, resolution for the output
    """
    dot = Digraph(comment="Element Tree")
    dot.attr('node', shape='box', style='filled', color='black', width='1', height='1', fontname='Calibri', fontsize='12', fontcolor='black')
    # **Add this line to make the edges orthogonal (90-degree)**
    dot.attr('graph', splines='ortho', rankdir='TB')  # 'TB' stands for top-bottom direction
    dot.attr('edge', arrowhead='none')
    dot.attr(label=filename, labelloc="t", fontsize="24", fontname='Calibri')

    colors = {
        0: {'fillcolor': '#001f3f', 'fontcolor': 'white', 'fontname': 'Calibri'},  # Root: Dark blue, white font
        1: {'fillcolor': '#0074D9', 'fontcolor': 'white', 'fontname': 'Calibri'},  # Child: Blue, white font
        2: {'fillcolor': '#7FDBFF', 'fontcolor': 'black', 'fontname': 'Calibri'},  # Sub-child: Light blue, black font
        3: {'fillcolor': '#DDDDDD', 'fontcolor': 'black', 'fontname': 'Calibri'}   # Sub-sub-child: Light gray, black font
    }

    # Recursive function to add nodes and edges, supporting empty levels
    def add_nodes_and_edges(parent, children, level):
        # Create the parent node with custom display name
        dot.node(parent, elements_names.get(parent, parent), fillcolor=colors[level]['fillcolor'], 
                 fontcolor=colors[level]['fontcolor'], fontname=colors[level]['fontname'])
        
        # Add child nodes and edges
        for child in children:
            # Determine if the child has children (is a parent)
            if child in elements:
                # Recursively add child and subchildren
                add_nodes_and_edges(child, elements[child], level + 1)
            else:
                # Add a subchild node with a custom display name
                dot.node(child, elements_names.get(child, child), fillcolor=colors[level + 1]['fillcolor'], 
                         fontcolor=colors[level + 1]['fontcolor'], fontname=colors[level + 1]['fontname'])
            
            # Create edge between parent and child
            dot.edge(parent, child)
            

    # Start with the root node at level 0
    root = "Root"
    add_nodes_and_edges(root, elements.get(root, []), level=0)
    
    # Create the legend
    with dot.subgraph(name='cluster_legend') as legend:
        legend.attr(label="Legend", fontsize="20", style="solid", rankdir="TB")
        legend.node("Legend_Root", "Root", fillcolor=colors[0]['fillcolor'], fontcolor=colors[0]['fontcolor'], fontname=colors[0]['fontname'])
        legend.node("Legend_Child", "Child", fillcolor=colors[1]['fillcolor'], fontcolor=colors[1]['fontcolor'], fontname=colors[1]['fontname'])
        legend.node("Legend_SubChild", "Sub-child", fillcolor=colors[2]['fillcolor'], fontcolor=colors[2]['fontcolor'], fontname=colors[2]['fontname'])
        legend.node("Legend_SubSubChild", "Sub-sub-child", fillcolor=colors[3]['fillcolor'], fontcolor=colors[3]['fontcolor'], fontname=colors[3]['fontname'])
        legend.edge("Legend_Root", "Legend_Child", style="invis")
        legend.edge("Legend_Child", "Legend_SubChild", style="invis")
        legend.edge("Legend_SubChild", "Legend_SubSubChild", style="invis")

    # Save the output as an SVG file
    output_filename = f"{filename}"
    dot.render(output_filename, format='svg')
    print(f"Graphical tree generated and saved as '{output_filename}'")
