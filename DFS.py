import networkx as nx
import matplotlib.pyplot as plt


# Function for Depth First Search (DFS)
def depth_first_search(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")  # Show the current visiting node

    for neighbor in graph[start]:
        if neighbor not in visited:
            depth_first_search(graph, neighbor, visited)


# Input validation for integer values
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Input validation for starting node
def get_valid_start_node(graph):
    while True:
        start_node = input("Please enter the starting node for DFS: ")
        if start_node in graph:
            return start_node
        else:
            print(f"Error: Node '{start_node}' is not in the graph. Please try again.")


# Build graph from user input with validation
def build_graph():
    graph = {}
    n = get_positive_integer("Please enter the number of nodes: ")
    e = get_positive_integer("Please enter the number of edges: ")

    # Create the graph
    G = nx.DiGraph()  # Directed graph (use nx.Graph() if undirected)

    # Input node names with validation
    nodes = []
    print("Please enter the names of the nodes:")
    for i in range(n):
        while True:
            node = input(f"Node {i+1}: ").strip()
            if node and node not in nodes:
                graph[node] = []
                nodes.append(node)
                G.add_node(node)
                break
            else:
                print("Invalid input. Please enter a unique name for each node.")

    # Input edges with validation
    print("\nPlease enter the edges:")
    for i in range(e):
        while True:
            try:
                u, v = input(f"Edge {i+1} (e.g., A B): ").split()
                if u in graph and v in graph:
                    graph[u].append(v)
                    G.add_edge(u, v)
                    break
                else:
                    print("Invalid edge. Both nodes must exist in the list of nodes.")
            except ValueError:
                print("Invalid format. Please enter in the format 'Node1 Node2'.")

    return graph, G


# Receive the graph and generate the visualization
graph, G = build_graph()

# Input the starting node with validation
start_node = get_valid_start_node(graph)

# Perform DFS and show results
print("\nDFS Results:")
depth_first_search(graph, start_node)

# Graph Visualization
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', node_size=3000, font_size=12)
plt.title("Graph Visualization", fontsize=16)
plt.show()
