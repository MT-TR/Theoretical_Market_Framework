# Import the function from graphical_tree.py
from graphical_tree import create_graphical_tree

# Define the tree structure with parent-child relationships
tree_elements = {
    "Root": ["Child 1", "Child 2"],
    "Child 1": ["Sub-child 1", "Sub-child 2"],
    "Child 2": ["Sub-child 3"],
    "Sub-child 1": ["Sub-sub-child 1"],
}

# Provide the filename for the output SVG
output_filename = "my_tree_diagram"

# Call the function with the tree structure and output filename
create_graphical_tree(tree_elements, filename=output_filename)