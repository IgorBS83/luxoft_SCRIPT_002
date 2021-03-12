class Graph:
    def __init__(self, vertex_name):
        self.vertex_list = [Vertex(vertex_name)]
        self.edge_list = []
        self.current_vertex = self.vertex_list[0]
    def add_vertex(self, vertex_name):
        self.vertex_list.append(Vertex(vertex_name))
    def find_vertex(self, vertex_name):
        for i_vertex in self.vertex_list:
            if i_vertex.get_name() == vertex_name:
                return i_vertex
        return Vertex("None")
    def add_edge(self, src_name, dst_name):
        src_vertex = self.find_vertex(src_name)
        dst_vertex = self.find_vertex(dst_name)
        if src_vertex.get_name() == "None":
            print("No source Vertex")
        elif dst_vertex.get_name() == "None":
            print("No destination Vertex")
        else:
            self.edge_list.append(Edge(src_vertex, dst_vertex))
    def set_current_vertex(self, dst_name):
        dst_vertex = self.find_vertex(dst_name)
        if dst_vertex.get_name() == "None":
            print("No destination Vertex")
        else:
            found_edge = self.current_vertex.get_edge_for_connected_vertex(self.edge_list, dst_vertex)
            if found_edge == "None":
                return "None"
            else:
                self.current_vertex = found_edge.get_connected_vertex()

class Vertex:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def get_edge_for_connected_vertex(self, edge_list, dst_vertex):
        is_found = False
        for i_edge in edge_list:
            if self == i_edge.src_vertex:
                if dst_vertex == i_edge.get_connected_vertex():
                    return i_edge
        if is_found == False:
            return "None"


class Edge:
    def __init__(self, src, dst):
        self.src_vertex = src
        self.dst_vertex = dst
    def get_connected_vertex(self):
        return self.dst_vertex

bot_graph = Graph("v1")
bot_graph.add_vertex("v2")
bot_graph.add_edge("v1", "v2")
bot_graph.set_current_vertex("v2")
bot_graph.add_vertex("v3")
bot_graph.add_edge("v2", "v3")
bot_graph.set_current_vertex("v3")
bot_graph.add_edge("v3", "v1")
bot_graph.set_current_vertex("v1")
bot_graph.set_current_vertex("v3")

# print(bot_graph.get_name())
