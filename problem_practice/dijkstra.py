import math
from heapq import heappush, heappop

#node
class Node:
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.distance = math.inf # 從出發點的距離
        self.previous = None #前一個點

    def _add_edge(self, edge):
       self.edges.append(edge)

    def __lt__(self, other):
       if self.id == other.id:
          return True
       return self.distance < other.distance


#edge
class Edge:
    def __init__(self, src, dest, weight):
        self.source = src
        self.destination = dest
        self.weight = weight

#graph
class Graph:
  def __init__(self,):
    self.nodes = {}

  def add_node(self, node_id):
    if node_id not in self.nodes:
      self.nodes[node_id] = Node(node_id)
    return self.nodes[node_id]

  def add_edge(self, src_id, dest_id, weight: int):
    src = self.add_node(src_id)
    dest = self.add_node(dest_id)
    edge = Edge(src, dest, weight)
    src._add_edge(edge)


def dijkstra(graph, start_id):
    """
    Implementation of Dijkstra's shortest path algorithm.

    Args:
        graph: Graph object containing nodes and edges
        start_id: ID of the starting node

    Returns:
        Dictionary of node_id: shortest distance from start node
    """
    # Initialize distances
    for node in graph.nodes.values():
        node.distance = math.inf
        node.previous = None

    # set start_node distance to 0
    start_node = graph.nodes[start_id]
    start_node.distance = 0

    # Priority queue to store nodes
    pq = []
    heappush(pq, start_node)

    # Set to keep track of visited nodes
    # visited 意思是說該節點已經被檢查過所有可到達的鄰近節點的距離並且更新了
    visited = set()

    while pq:
        curr_node = heappop(pq)

        if curr_node.id in visited:
            continue

        visited.add(curr_node)

        for edge in curr_node.edges:
           neighbor = edge.destination
           if neighbor.id in visited:
              continue

           distance = curr_node.distance + edge.weight
           if distance < neighbor.distance:
              neighbor.distance = distance
              neighbor.previous = curr_node
              heappush(pq, neighbor)

    distances = {node_id: node.distance for node_id, node in graph.nodes.items()}
    return distances


def get_shortest_path(graph, start_id, end_id):
    distances = dijkstra(graph, start_id)

    path = []
    curr_node = distances[end_id]
    while curr_node:
       path.append(curr_node.previous)
       curr_node = curr_node.previous

    return path[-1::-1]
