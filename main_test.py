# Import the function from graphical_tree.py
from fn_graphical_tree import create_graphical_tree

elements = {
    # Root node
    "Root": ["Remuneration_scheme", "Bid_properties"],

    # Options under 'Remuneration scheme'
    "Remuneration_scheme": ["No_remuneration", "Negotiated_price", "Pay_as_bid", "Uniform_pay_as_clear", "Non_uniform_pay_as_clear", "Cost_based_remuneration"],

    # Bid properties with substructure
    "Bid_properties": ["Minimum_bid_size", "Bid_structure"],

    # Options under 'Minimum bid size'
    "Minimum_bid_size": ["Minimum_bid_size_value"],

    # Options under 'Bid structure'
    "Bid_structure": ["Simple", "Complex"]
}
elements_names = {
    # Root display name
    "Root": "Market operation",
    
    # Second-level categories (Pillars)
    "Remuneration_scheme": "Remuneration scheme",
    "Bid_properties": "Bid properties",
    
    # Options under 'Remuneration scheme'
    "No_remuneration": "No remuneration",
    "Negotiated_price": "Negotiated price",
    "Pay_as_bid": "Pay-as-bid",
    "Uniform_pay_as_clear": "Uniform pay-as-clear",
    "Non_uniform_pay_as_clear": "Non-uniform pay-as-clear (i.e., nodal pricing)",
    "Cost_based_remuneration": "Cost-based remuneration",

    # Bid properties
    "Minimum_bid_size": "Minimum bid size",
    "Bid_structure": "Bid structure",

    # Options under 'Bid structure'
    "Simple": "Simple",
    "Complex": "Complex",

    # Option under 'Minimum bid size'
    "Minimum_bid_size_value": "Minimum bid size value"
}

# Call the function to create the tree
create_graphical_tree(elements, elements_names, filename='market_operation_tree2')
