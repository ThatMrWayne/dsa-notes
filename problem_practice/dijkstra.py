import math

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



# 處理 decreasing key 狀況
# 需要自己實作 pq


class MinHeap:
    def __init__(self):
        self.array = []
        self.index_map = dict() #{Node: array index}

    def __repr__(self):
        return f"{[i.distance for i in self.array]}"

    def empty(self):
        return len(self.array) == 0

    def push(self, item: Node):
        if item in self.index_map:
            return
        self.array.append(item)
        if len(self.array) == 1:
            self.index_map[item] = 0
        else: # bubble up process
            curr_idx = len(self.array)-1
            parent_idx = ((curr_idx+1)//2)-1
            while True:
                parent_node = self.array[parent_idx]
                if self.array[curr_idx] < self.array[parent_idx]:
                    self.array[curr_idx], self.array[parent_idx] = self.array[parent_idx], self.array[curr_idx]
                    self.index_map[parent_node] = curr_idx
                else:
                    break
                curr_idx = parent_idx
                if curr_idx == 0:
                   break
                parent_idx = ((curr_idx+1)//2)-1
            self.index_map[item] = curr_idx

    def popmin(self):
        last_item = self.array[-1]
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        min_item = self.array.pop()
        del self.index_map[min_item]
        # bubble down
        smallest = curr_idx = 0
        left_child_idx = ((curr_idx+1)*2)-1
        right_child_idx = (((curr_idx+1)*2)+1)-1
        while True:
            if left_child_idx < len(self.array) and self.array[left_child_idx] < self.array[smallest]:
                smallest = left_child_idx
            if right_child_idx < len(self.array) and self.array[right_child_idx] < self.array[smallest]:
                smallest = right_child_idx
            if smallest == curr_idx:
                break
            else:
                smallest_node = self.array[smallest]
                self.array[curr_idx], self.array[smallest] = self.array[smallest], self.array[curr_idx]
                self.index_map[smallest_node] = curr_idx
                curr_idx = smallest
                left_child_idx = ((curr_idx+1)*2)-1
                right_child_idx = (((curr_idx+1)*2)+1)-1
        self.index_map[last_item] = curr_idx
        return min_item

    def get_item_index(self, item: Node):
       return self.index_map[item]

    def is_in_heap(self, item):
       return item in self.index_map

    def decrease_key(self, item: Node, new_priority):
        if not self.is_in_heap(item):
            return
        item.distance = new_priority
        curr_idx = self.get_item_index(item)
        if curr_idx == 0:
            return
        parent_idx = ((curr_idx+1)//2)-1
        while True:
            parent_node = self.array[parent_idx]
            if self.array[curr_idx] < self.array[parent_idx]:
                self.array[curr_idx], self.array[parent_idx] = self.array[parent_idx], self.array[curr_idx]
                self.index_map[parent_node] = curr_idx
            else:
                break
            curr_idx = parent_idx
            if curr_idx == 0:
                break
            parent_idx = ((curr_idx+1)//2)-1
        self.index_map[item] = curr_idx


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
    pq = MinHeap()
    pq.push(start_node)

    # Set to keep track of visited nodes
    # visited 意思是說該節點已經被檢查過所有可到達的鄰近節點的距離並且更新了
    visited = set()

    while not pq.empty():
        curr_node = pq.popmin()

        if curr_node.id in visited:
            continue

        visited.add(curr_node.id)

        for edge in curr_node.edges:
            neighbor = edge.destination
            if neighbor.id in visited:
               continue

            distance = curr_node.distance + edge.weight
            if distance < neighbor.distance:
                # there might be decreasing key situation
                if pq.is_in_heap(neighbor):
                    pq.decrease_key(neighbor, distance)
                else:
                    neighbor.distance = distance
                    pq.push(neighbor)
                neighbor.previous = curr_node

    distances = {node_id: node.distance for node_id, node in graph.nodes.items()}
    return distances


def get_shortest_path(graph, start_id, end_id):
    dijkstra(graph, start_id)

    path = []
    curr_node = graph.nodes[end_id]
    while curr_node:
       path.append(curr_node.id)
       curr_node = curr_node.previous

    return path[-1::-1]


def main():
    # Create a graph
    g = Graph()

    # Add edges (source, destination, weight)
    edges = [
        (0, 1, 4), (0, 2, 2),
        (1, 2, 1), (1, 3, 5),
        (2, 3, 8), (2, 4, 10),
        (3, 4, 2), (3, 5, 6),
        (4, 5, 3)
    ]

    for source, dest, weight in edges:
        g.add_edge(source, dest, weight)

    # Find shortest distances from node 0
    distances = dijkstra(g, 0)
    #print("Shortest distances from node 0:", distances)


if __name__ == "__main__":
    main()
