from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    id: int
    is_visited: bool = False


@dataclass
class Edge:
    start_node: Node
    end_node: Node

    def get_other_node(self, node_id: int) -> Node:
        if self.start_node.id == node_id:
            return self.end_node
        else:
            return self.start_node


@dataclass
class Graph:
    nodes: dict
    adjacent_edges: dict

    def get_node(self, node_id: int) -> Node:
        return self.nodes[node_id]

    def set_node_visited(self, node_id: int):
        self.nodes[node_id].is_visited = True

    def get_connected_nodes(self, node_id: int) -> List[Node]:
        adjacent_edges = self.adjacent_edges.get(node_id, [])
        return [edge.get_other_node(node_id) for edge in adjacent_edges]


def BFS(graph: Graph, start_node_id: int):
    queue = [graph.get_node(start_node_id)]
    stage = 0

    while len(queue) > 0:
        stage += 1

        node = queue.pop(0)
        print("방문한 노드: {:d}".format(node.id))

        if node.is_visited:
            continue

        print()
        print("탐색 {:d}".format(stage))

        graph.set_node_visited(node.id)
        queue += graph.get_connected_nodes(node.id)

        print("QUEUE: ", [node.id for node in queue])


if __name__ == "__main__":
    nodes = {}
    for i in range(6):
        nodes[i + 1] = Node(id=i + 1)

    adjacent_edges = {}
    adjacent_edges[1] = [Edge(start_node=nodes[1], end_node=nodes[2])]
    adjacent_edges[1] += [Edge(start_node=nodes[1], end_node=nodes[3])]
    adjacent_edges[2] = [Edge(start_node=nodes[2], end_node=nodes[4])]
    adjacent_edges[2] += [Edge(start_node=nodes[2], end_node=nodes[5])]
    adjacent_edges[2] += [Edge(start_node=nodes[2], end_node=nodes[6])]
    adjacent_edges[3] = [Edge(start_node=nodes[3], end_node=nodes[4])]
    adjacent_edges[5] = [Edge(start_node=nodes[5], end_node=nodes[6])]

    graph = Graph(nodes=nodes, adjacent_edges=adjacent_edges)
    BFS(graph, 1)