from dataclasses import dataclass
from typing import List
import pprint


@dataclass
class Node:
    id: int
    is_visited: bool = False


@dataclass
class Edge:
    start_node: Node
    end_node: Node
    weight: float

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


def floyd_warshall(graph: Graph) -> dict:
    path = {}
    nodes = graph.nodes
    # 모든 노드에서 노드로 이어지는 path를 초기화
    for _, node in nodes.items():
        path[node.id] = {}
        for _, other_node in nodes.items():
            if node.id != other_node.id:
                path[node.id][other_node.id] = float("inf")
            else:
                path[node.id][other_node.id] = 0
        # 인접한 노드끼리의 최단 거리는 가중치값과 동일하므로 가중치값으로 초기화
        for adjacent_edge in graph.get_adjacent_edges(node.id):
            other_node = adjacent_edge.get_other_node(node.id)
            path[node.id][other_node.id] = adjacent_edge.get_weight()

    # 시작 노드, 끝 노드로 직접 이어지는 경로가 빠른지, 경유해서 가는 경우가 빠른지 확인
    # 위에서 초기화하지 않을 경우 for문이 돌지 않은 곳의 값이 inf 임으로 계산 불가
    for _, pivot_node in nodes.items():
        for _, start_node in nodes.items():
            for _, end_node in nodes.items():
                path[start_node.id][end_node.id] = min(
                    path[start_node.id][end_node.id],
                    path[start_node.id][pivot_node.id] + path[pivot_node.id][end_node.id],
                )
    return path


if __name__ == "__main__":
    nodes = {}
    for i in range(6):
        nodes[i + 1] = Node(id=i + 1)

    adjacent_edges = {}
    adjacent_edges[1] = [Edge(start_node=nodes[1], end_node=nodes[2], weight=5)]
    adjacent_edges[1] += [Edge(start_node=nodes[1], end_node=nodes[3], weight=4)]
    adjacent_edges[2] = [Edge(start_node=nodes[2], end_node=nodes[4], weight=3)]
    adjacent_edges[2] += [Edge(start_node=nodes[2], end_node=nodes[5], weight=2)]
    adjacent_edges[2] += [Edge(start_node=nodes[2], end_node=nodes[6], weight=10)]
    adjacent_edges[3] = [Edge(start_node=nodes[3], end_node=nodes[4], weight=1)]
    adjacent_edges[5] = [Edge(start_node=nodes[5], end_node=nodes[6], weight=6)]

    graph = Graph(nodes=nodes, adjacent_edges=adjacent_edges)
    pprint.pprint(floyd_warshall(graph=graph))