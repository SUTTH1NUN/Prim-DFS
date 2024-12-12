import heapq
import networkx as nx
import matplotlib.pyplot as plt


def prim_algorithm(graph, start):
    """
    Prim's Algorithm to find Minimum Spanning Tree (MST) from a starting node in a weighted undirected graph.
    """

    # Min-heap to maintain edges with minimum weight
    visited = set()
    min_heap = [(0, start, -1)]
    mst_edges = []

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)

        if parent != -1:
            mst_edges.append((parent, node, weight))

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, node))

    return mst_edges


def draw_graph(graph, mst_edges, reverse_mapping):
    """
    Draw the full graph and highlight the MST edges.
    """
    G = nx.Graph()

    # Add all edges into Graph
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)

    # Draw the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, labels=reverse_mapping, node_color='lightblue', node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=[(edge[0], edge[1]) for edge in mst_edges], edge_color='red', width=2)

    # Annotate edge weights
    edge_labels = {(edge[0], edge[1]): edge[2] for edge in mst_edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Graph with MST Highlighted in Red")
    plt.show()


# Input for number of nodes and edges
num_nodes = int(input("Enter the number of nodes (e.g., 4 for a, b, c, d): "))
num_edges = int(input("Enter the number of edges: "))
# Create mapping of node letters to indices and reverse
node_mapping = {}
reverse_mapping = {}
for i in range(num_nodes):
    node_mapping[chr(ord('a') + i)] = i
    reverse_mapping[i] = chr(ord('a') + i)

# Create adjacency list
graph = {i: [] for i in range(num_nodes)}

# Input edges
print("Enter the edges in the format: node1 node2 weight (e.g., a b 4)")
for _ in range(num_edges):
    u, v, w = input().split()
    u_idx, v_idx = node_mapping[u], node_mapping[v]
    graph[u_idx].append((v_idx, int(w)))
    graph[v_idx].append((u_idx, int(w)))  # Undirected graph

# Run the Prim's algorithm
mst = prim_algorithm(graph, start=0)

# Output the result
print("\nEdges in the Minimum Spanning Tree:")
for edge in mst:
    print(reverse_mapping[edge[0]], "-", reverse_mapping[edge[1]], f"(weight: {edge[2]})")

# Calculate the sum of weights of all edges in the MST
total_weight = sum(edge[2] for edge in mst)
print(f"\nTotal weight of all edges in the MST: {total_weight}")

# Draw the graph with MST highlighted
draw_graph(graph, mst, reverse_mapping)
