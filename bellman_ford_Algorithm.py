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
    weight: float
    # 가중치를 설정
    def get_weight(self) -> float:
        return self.weight

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

    def get_adjacent_edges(self, node_id: int) -> List[Edge]:
        return self.adjacent_edges.get(node_id, [])

    def set_edge_weight(self, edge_id: int, weight: float):
        self.edges[edge_id].set_weight(weight)

def bellmanford(graph, start_node_id):
    distances = {}
    path_map = {}
    for _, node in graph.nodes.items():
        distances[node.id] = float("inf")
        path_map[node.id] = None
    distances[start_node_id] = 0

    for node in graph.nodes: # node의 개수만큼 반복 (전체 범위를 탐색)
        for _, edges in graph.adjacent_edges.items():
            for edge in edges:
                # edge에 저장된 가중치와 start node의 거리를 더함
                tmp = distances[edge.start_node.id] + edge.get_weight()
                # 만약 더한 값이 저장된 end node의 거리보다 작다면
                if tmp < distances[edge.end_node.id]:
                    # end node의 값을 업데이트
                    distances[edge.end_node.id] = tmp
                    # path map에 end_node가 어디서 왔는지 저장
                    path_map[edge.end_node.id] = edge.start_node.id

    return distances, path_map


if __name__ == "__main__":
    nodes = {}
    for i in range(6):
        nodes[i+1] = Node(id=i+1)

    adjacent_edges = {}
    adjacent_edges[1] = [Edge(start_node=nodes[1], end_node=nodes[2], weight=1)]
    adjacent_edges[1] += [Edge(start_node=nodes[1], end_node=nodes[3], weight=1)]
    adjacent_edges[2] = [Edge(start_node=nodes[2], end_node=nodes[4], weight=1)]
    adjacent_edges[2] += [Edge(start_node=nodes[2], end_node=nodes[5], weight=1)]
    adjacent_edges[2] += [Edge(start_node=nodes[2], end_node=nodes[6], weight=10)]
    adjacent_edges[3] = [Edge(start_node=nodes[3], end_node=nodes[4], weight=1)]
    adjacent_edges[5] = [Edge(start_node=nodes[5], end_node=nodes[6], weight=1)]

    graph = Graph(nodes=nodes, adjacent_edges=adjacent_edges)
    print(bellmanford(graph, 1))