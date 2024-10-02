from graphviz import Digraph
# Import the function from graphical_tree.py
from fn_graphical_tree import create_graphical_tree

# Define the elements (parent-child relationships) for the tree
elements = {
    # Root node
    "Root": ["Remuneration_scheme", "Remuneration_of_product_attribute", "Market_clearing_type", "Procurement_frequency", "Bid_properties"],

    # Children of 'Remuneration_scheme'
    "Remuneration_scheme": ["No_remuneration", "Negotiated_price", "Pay_as_bid", "Uniform_pay_as_clear", "Non_uniform_pay_as_clear", "Cost_based_remuneration"],

    # Children of 'Remuneration_of_product_attribute'
    "Remuneration_of_product_attribute": ["Availability", "Activation", "Availability_and_Activation"],

    # Children of 'Market_clearing_type'
    "Market_clearing_type": ["Continuous", "Discrete"],

    # Children of 'Procurement_frequency'
    "Procurement_frequency": ["Event_based_on_SO_call", "Daily", "Weekly", "Monthly", "Other"],

    # Children of 'Bid_properties'
    "Bid_properties": ["Minimum_bid_size", "Bid_structure"],

    # Children of 'Bid_structure'
    "Bid_structure": ["Simple", "Complex"],

    # Children of 'Minimum_bid_size'
    "Minimum_bid_size": ["Minimum_bid_size_value"]
}


# Define the display names for each element
elements_names = {
    # Root display name
    "Root": "Market operation",
    
    # Second-level categories
    "Remuneration_scheme": "Remuneration scheme",
    "Remuneration_of_product_attribute": "Remuneration of the product attribute",
    "Market_clearing_type": "Market-clearing type",
    "Procurement_frequency": "Procurement frequency",
    "Bid_properties": "Bid properties",
    
    # Third-level items under 'Remuneration_scheme'
    "No_remuneration": "No remuneration",
    "Negotiated_price": "Negotiated price",
    "Pay_as_bid": "Pay-as-bid",
    "Uniform_pay_as_clear": "Uniform pay-as-clear",
    "Non_uniform_pay_as_clear": "Non-uniform pay-as-clear (i.e., nodal pricing)",
    "Cost_based_remuneration": "Cost-based remuneration",

    # Items under 'Remuneration_of_product_attribute'
    "Availability": "Availability",
    "Activation": "Activation",
    "Availability_and_Activation": "Availability and Activation\nFor: Active power, Reactive power, Apparent power",

    # Items under 'Market_clearing_type'
    "Continuous": "Continuous",
    "Discrete": "Discrete",

    # Items under 'Procurement_frequency'
    "Event_based_on_SO_call": "Event-based on SO call",
    "Daily": "Daily",
    "Weekly": "Weekly",
    "Monthly": "Monthly",
    "Other": "Other",

    # Items under 'Bid_properties'
    "Minimum_bid_size": "Minimum bid size",
    "Bid_structure": "Bid structure",

    # Items under 'Bid_structure'
    "Simple": "Simple",
    "Complex": "Complex",

    # Item under 'Minimum_bid_size'
    "Minimum_bid_size_value": "Minimum bid size value"
}


# Call the function to create the tree
create_graphical_tree(elements, elements_names, filename='market_operation_tree')
