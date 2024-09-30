from graphviz import Digraph

def create_graphical_tree(elements, dpi=600):
    """Creates a graphical tree using Graphviz"""
    dot = Digraph(comment="Element Tree")
    # Define default node shape as square (box)
    #dot.attr('node', shape='box'
    #dot.attr('node', shape='box', width='1', height='1'))
    dot.attr('node', shape='box', style='filled', color='black', width='1', height='1', fontname='Calibri', fontsize='12', fontcolor='black')
    # Set default edge attributes to remove arrows
    dot.attr('edge', arrowhead='none')

    # Color assignments for different levels
    colors = {
        0: 'lightblue',    # Root level
        1: 'lightgreen',   # First child level
        2: 'lightyellow',  # Sub-child level
        3: 'lightcoral'    # Sub-sub-child level (if applicable)
    }

    # Recursive function to add nodes with the same color per level
    def add_nodes_and_edges(parent, children, level):
        # Add the parent node with the color for the current level
        dot.node(parent, parent, fillcolor=colors[level])
        
        # Add child nodes and edges
        for child in children:
            # Determine if the child has its own children
            if child in elements:
                # Recursively add sub-children with the next level's color
                add_nodes_and_edges(child, elements[child], level + 1)
            else:
                # Add sub-child node with the next level's color
                dot.node(child, child, fillcolor=colors[level + 1])
            
            # Create the edge (relationship between parent and child)
            dot.edge(parent, child)

    # Start the tree with the root node at level 0
    root = "Root"
    add_nodes_and_edges(root, elements[root], level=0)
    
    # Create a separate legend as a subgraph
    with dot.subgraph(name='cluster_legend') as legend:
        legend.attr(label="Legend", fontsize="20", style="dashed")
        
        # Add legend nodes (not part of the main plot)
        legend.node("Legend_Root", "Root", fillcolor='lightblue', color='black')
        legend.node("Legend_Child", "Child", fillcolor='lightgreen', color='black')
        legend.node("Legend_SubChild", "Sub-child", fillcolor='lightyellow', color='black')
        legend.node("Legend_SubSubChild", "Sub-sub-child", fillcolor='lightcoral', color='black')

        # Make sure these are placed independently in the legend cluster
        legend.attr(rankdir="LR")  # Horizontal layout for the legend
        legend.edge("Legend_Root", "Legend_Child", style="invis")  # Invisible edges just for layout
        legend.edge("Legend_Child", "Legend_SubChild", style="invis")
        legend.edge("Legend_SubChild", "Legend_SubSubChild", style="invis")

    
    # Set the DPI for higher image quality
    #dot.attr(dpi=str(dpi)) # valid only if format is 'svg'
    # Render the tree to an image file
    dot.render('element_tree', format='svg') #format='png'
    print("Graphical tree generated and saved as 'element_tree'")

# Define the tree structure with parent-child relationships
tree_elements = {
    "Root": ["Child 1", "Child 2"],
    "Child 1": ["Sub-child 1", "Sub-child 2"],
    "Child 2": ["Sub-child 3"],
    "Sub-child 1": ["Sub-sub-child 1"],
}

if __name__ == "__main__":
    # Create and render the graphical tree
    create_graphical_tree(tree_elements)
