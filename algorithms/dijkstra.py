from queue import PriorityQueue
class Node:
    def __init__(self, val):
        self.val = val
        self.adj = []
    
    def add_adj(self, cost, n):
        self.adj.append((cost, n))
    
    def __lt__(self, other):
        return self.val < other.val
    # def __hash__(self):
    #     pass

def dijkstra(start_vertex, all_nodes):
    visited = set()
    D = { v:float('inf') for v in all_nodes }
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (_, current_vertex) = pq.get()
        visited.add(current_vertex)

        for neighbor in current_vertex.adj:
            distance, node = neighbor
            if node not in visited:
                old_cost = D[node]
                new_cost = D[current_vertex] + distance
                
                if new_cost < old_cost:
                    pq.put((new_cost, node))
                    D[node] = new_cost
    return D