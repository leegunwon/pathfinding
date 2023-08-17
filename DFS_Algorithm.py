from dataclasses import dataclass
from typing import List

STAGE = 1

@dataclass
class Node:
    id: int
    is_visited: bool = False

@dataclass
class Edge:
    start_node: Node
    end_node: Node

    def get_other_node(self, node_id: int) -> Node:
        # start_node와 현재 node가 같다면 end_node와 현재 node가 연결되어 있음
        if self.start_node.id == node_id:
            return self.end_node
        # start_node와 현재 node가 다르다면 현재 node가 end_node와 같을 것이므로 start_node와 현재 node가 연결되어 있음
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
    # get 함수를 이용해 딕셔너리에 저장되어 있는 인접해 있는 노드들을 반환하는 함수
    def get_connected_nodes(self, node_id: int) -> List[Node]:
        adjacent_edges = self.adjacent_edges.get(node_id, [])
        return [edge.get_other_node(node_id) for edge in adjacent_edges]

def DFS(graph: Graph, start_node_id: int):
    global STAGE
    graph.set_node_visited(start_node_id)
    print("탐색 {:d}".format(STAGE))
    print("방문한 노드: {:d}".format(start_node_id))
    print()

    for connected_node in graph.get_connected_nodes(start_node_id):
        print(connected_node.id)
        if connected_node.is_visited:
            continue
        STAGE += 1
        DFS(graph, connected_node.id)



if __name__ == "__main__":
    nodes = {}
    for i in range(6):
        nodes[i+1] = Node(id=i+1)

    adjacent_edges = {}
    adjacent_edges[1] = [Edge(start_node=nodes[1], end_node=nodes[2])]
    adjacent_edges[1] += [Edge(start_node=nodes[1], end_node=nodes[3])]
    adjacent_edges[2] = [Edge(start_node=nodes[2], end_node=nodes[4])]
    adjacent_edges[2] += [Edge(start_node=nodes[2], end_node=nodes[5])]
    adjacent_edges[2] += [Edge(start_node=nodes[2], end_node=nodes[6])]
    adjacent_edges[3] = [Edge(start_node=nodes[3], end_node=nodes[4])]
    adjacent_edges[5] = [Edge(start_node=nodes[5], end_node=nodes[6])]

    graph = Graph(nodes=nodes, adjacent_edges=adjacent_edges)
    DFS(graph, 1)