from graphviz import Digraph

def create_graphical_tree(elements, dpi=600):
    """Creates a graphical tree using Graphviz"""
    dot = Digraph(comment="Element Tree")
    # Define default node shape as square (box)
    #dot.attr('node', shape='box'
    #dot.attr('node', shape='box', width='1', height='1'))
    dot.attr('node', shape='box', style='filled', color='lightblue', width='1', height='1', fontname='Calibri', fontsize='12', fontcolor='black')


    # Add nodes and relationships based on elements
    for parent, children in elements.items():
        # Add the parent node
        dot.node(parent, parent)
        
        # Add child nodes and connections
        for child in children:
            dot.node(child, child)
            dot.edge(parent, child)

    # Render the tree to an image file
    dot.render('element_tree', format='svg') #format='svg'
    print("Graphical tree generated and saved as 'element_tree.png'")

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
