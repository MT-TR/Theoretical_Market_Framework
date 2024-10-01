# Import the function from graphical_tree.py
from graphical_tree import create_graphical_tree

# Define the tree structure with parent-child relationships
tree_elements_structure = {
    "Root": ["Child 1", "Child 2"],
    "Child 1": ["Sub-child 1", "Sub-child 2"],
    "Child 2": ["Sub-child 3"],
    "Sub-child 1": ["Sub-sub-child 1"],
}

tree_elements_names = {
    "Root": ["Child A", "Child B"],
    "Child 1": ["Sub-child A", "Sub-child B"],
    "Child 2": ["Sub-child C"],
    "Sub-child 1": ["Sub-sub-child A"],
}



# tree_elements = {
#     "Root": ["Remuneration scheme", "Remuneration of the product attribute","Market-clearing type","Procurement frequency","Bid properties"],
#     "Remuneration scheme": [""],
#     "Remuneration of the product attribute": [],
#     "Child 2": ["Sub-child 3"],
#     "": ["Sub-sub-child 1"],
# }









# Provide the filename for the output SVG
output_filename = "my_tree_diagram2"

# Call the function with the tree structure and output filename
create_graphical_tree(tree_elements_structure, tree_elements_names, filename=output_filename)