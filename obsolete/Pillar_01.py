from graphviz import Digraph

def create_pillar01_tree(output_filename="market_operation_tree.svg"):
    # Initialize the Digraph object with rankdir TB (top to bottom)
    dot = Digraph("Market Operation", filename=output_filename, format="svg")
    dot.attr(rankdir="TB", size="10,10", splines="ortho", nodesep="0.5", ranksep="1")

    # Define colors for different levels
    colors = [
        {'fillcolor': '#0b5394', 'fontcolor': 'white', 'label': 'Pillar'},     # Dark blue (Root)
        {'fillcolor': '#6fa8dc', 'fontcolor': 'white', 'label': 'Feature'},    # Blue (Child)
        {'fillcolor': '#b6d7a8', 'fontcolor': 'black', 'label': 'Sub-feature'},# Light blue (Sub-child)
        {'fillcolor': '#d9d9d9', 'fontcolor': 'black', 'label': 'Options'},    # Light gray (Last level)
    ]

    # Add the root node (Pillar level)
    dot.node("root", "Market operation", shape="box", style="filled", 
             fontname="Calibri", fontsize="14", fillcolor=colors[0]['fillcolor'], 
             fontcolor=colors[0]['fontcolor'], color="black", width="2", height="2")

    # Add the child nodes (Feature level)
    dot.node("child1", "Remuneration\nscheme", shape="box", style="filled", 
             fontname="Calibri", fontsize="12", fillcolor=colors[1]['fillcolor'], 
             fontcolor=colors[1]['fontcolor'], color="black")
    dot.node("child2", "Remuneration of\nthe product\nattribute", shape="box", style="filled", 
             fontname="Calibri", fontsize="12", fillcolor=colors[1]['fillcolor'], 
             fontcolor=colors[1]['fontcolor'], color="black")
    dot.node("child3", "Market-clearing\ntype", shape="box", style="filled", 
             fontname="Calibri", fontsize="12", fillcolor=colors[1]['fillcolor'], 
             fontcolor=colors[1]['fontcolor'], color="black")
    dot.node("child4", "Procurement\nfrequency", shape="box", style="filled", 
             fontname="Calibri", fontsize="12", fillcolor=colors[1]['fillcolor'], 
             fontcolor=colors[1]['fontcolor'], color="black")
    dot.node("child5", "Bid properties", shape="box", style="filled", 
             fontname="Calibri", fontsize="12", fillcolor=colors[1]['fillcolor'], 
             fontcolor=colors[1]['fontcolor'], color="black")

    # Add edges between root and child nodes
    dot.edge("root", "child1")
    dot.edge("root", "child2")
    dot.edge("root", "child3")
    dot.edge("root", "child4")
    dot.edge("root", "child5")

    # Add sub-child nodes (Sub-feature level)
    dot.node("subchild1", "No remuneration\nNegotiated price\nPay-as-bid", shape="box", style="filled", 
             fontname="Calibri", fontsize="10", fillcolor=colors[3]['fillcolor'], 
             fontcolor=colors[3]['fontcolor'], color="black")
    dot.node("subchild2", "Availability\nActivation", shape="box", style="filled", 
             fontname="Calibri", fontsize="10", fillcolor=colors[3]['fillcolor'], 
             fontcolor=colors[3]['fontcolor'], color="black")
    dot.node("subchild3", "Continuous", shape="box", style="filled", 
             fontname="Calibri", fontsize="10", fillcolor=colors[3]['fillcolor'], 
             fontcolor=colors[3]['fontcolor'], color="black")
    dot.node("subchild4", "Event-based\non SO call\nDaily", shape="box", style="filled", 
             fontname="Calibri", fontsize="10", fillcolor=colors[3]['fillcolor'], 
             fontcolor=colors[3]['fontcolor'], color="black")
    dot.node("subchild5", "Minimum bid\nsize", shape="box", style="filled", 
             fontname="Calibri", fontsize="10", fillcolor=colors[3]['fillcolor'], 
             fontcolor=colors[3]['fontcolor'], color="black")
    dot.node("subchild6", "Simple\nComplex", shape="box", style="filled", 
             fontname="Calibri", fontsize="10", fillcolor=colors[3]['fillcolor'], 
             fontcolor=colors[3]['fontcolor'], color="black")

    # Add edges between child nodes and sub-child nodes
    dot.edge("child1", "subchild1")
    dot.edge("child2", "subchild2")
    dot.edge("child3", "subchild3")
    dot.edge("child4", "subchild4")
    dot.edge("child5", "subchild5")
    dot.edge("child5", "subchild6")

    # Create the legend as a separate cluster
    with dot.subgraph(name='cluster_legend') as legend:
        legend.attr(label="Legend", fontsize="20", style="solid", rankdir="LR")
        legend.node("Legend_Root", "Pillar", shape="box", style="filled", 
                    fontname="Calibri", fontsize="12", fillcolor=colors[0]['fillcolor'], 
                    fontcolor=colors[0]['fontcolor'], color="black")
        legend.node("Legend_Child", "Feature", shape="box", style="filled", 
                    fontname="Calibri", fontsize="12", fillcolor=colors[1]['fillcolor'], 
                    fontcolor=colors[1]['fontcolor'], color="black")
        legend.node("Legend_SubChild", "Sub-feature", shape="box", style="filled", 
                    fontname="Calibri", fontsize="12", fillcolor=colors[2]['fillcolor'], 
                    fontcolor=colors[2]['fontcolor'], color="black")
        legend.node("Legend_Options", "Options", shape="box", style="filled", 
                    fontname="Calibri", fontsize="12", fillcolor=colors[3]['fillcolor'], 
                    fontcolor=colors[3]['fontcolor'], color="black")

        # Create edges to structure the legend
        legend.edge("Legend_Root", "Legend_Child", style="invis")
        legend.edge("Legend_Child", "Legend_SubChild", style="invis")
        legend.edge("Legend_SubChild", "Legend_Options", style="invis")

    # Render the tree to an SVG file
    dot.render()


create_pillar01_tree("market_operation_tree.svg")