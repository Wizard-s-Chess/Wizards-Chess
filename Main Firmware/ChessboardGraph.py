import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
N=17
class PathGenerator:
    def __init__(self):
        self.last_position = (0,0)
    def draw_graph(self,G):
        plt.rcParams["figure.figsize"] = (30,30)
        pos = dict( (n, n) for n in G.nodes() )
        #labels = dict( ((i, j), i * N + j) for i, j in G.nodes() )
        color_map =  [('green' if (i%2 == 1 and j % 2 == 1) else 'blue') for i,j in G.nodes()]
        #color_map[get_id(source)] = 'red'
        #color_map[get_id(sink)] = 'yellow'
        nx.draw_networkx(G, pos=pos, node_color = color_map)

    
    def draw_shortest_path(self,G, path, path_edges):
        pos = dict( (n, n) for n in G.nodes() )
        nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=10)
        nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
        #plt.show()
    def remove_connecting_edges(self,G):
        for x in range(1, N, 2):
            for y in range(1, N, 2):
                for i in range(-1, 2):
                    for j in range (-1, 2):
                        u = (x, y)
                        v = (x+i, y+j)
                        if(x+i >=0 and y+j >=0 and G.has_edge(u, v)):
                            G.remove_edge(u, v)
    def remove_gutter_edges(self,G):
        for x in [0,N-1]:
            for y in range(17):
                for i in range(-1, 2):
                    for j in range (-1, 2):
                        u = (x, y)
                        v = (x+i, y+j)
                        if(x+i >=0 and y+j >=0 and G.has_edge(u, v)):
                            G.remove_edge(u, v)
        for y in [0,N-1]:
            for x in range(17):
                for i in range(-1, 2):
                    for j in range (-1, 2):
                        u = (x, y)
                        v = (x+i, y+j)
                        if(x+i >=0 and y+j >=0 and G.has_edge(u, v)):
                            G.remove_edge(u, v)


    def add_connecting_edges(self,G, u):
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = u[0]
                y = u[1]
                v= (x+i, y+j)
                if(x+i>=0 and y+j >=0 and x+i < N and y+j < N and u != v and ((x+i == x) or (y+j == y))):
                    G.add_edge(u, v)


    def get_coordinates_from_move(self,move):
        source = self.get_coordinates_from_uci(move[:2])
        sink = self.get_coordinates_from_uci(move[2:])
        return (source, sink)


    def convert_path_arduino(self,path):
        moves = []
        for (source, sink) in path:
            x_source = source[0]
            y_source = source[1]
            x_sink = sink[0]
            y_sink = sink[1]
            move = (x_source > x_sink) * 1 + (x_source < x_sink) * 2 + (y_source > y_sink) * 3 + (y_source < y_sink) * 4
            moves.append(str(move))
        return moves

    def get_path_source_sink(self,source,sink,is_restricted):
        
        G=nx.grid_2d_graph(N, N)
        H = G.copy()

        self.remove_connecting_edges(H)
        self.add_connecting_edges(H, source)
        self.add_connecting_edges(H, sink)
        if(is_restricted):
            self.remove_gutter_edges(H)
        path = nx.shortest_path(H,source=source, target=sink, method='dijkstra')
        path_edges = list(zip(path,path[1:]))
        self.draw_graph(H)
        self.draw_shortest_path(H,path,path_edges)
        moves = self.convert_path_arduino(path_edges)
        self.last_position = sink
        return "".join(moves)
    def get_path_to_cell(self,cell):
        source = self.last_position
        sink = self.get_coordinates_from_uci(cell)
        return self.get_path_source_sink(source,sink, False)

    def get_path_move(self,move):
        (source, sink) = self.get_coordinates_from_move(move)
        return self.get_path_source_sink(source,sink,True)
        
    def get_coordinates_from_uci(self,cell):
        cell = (ord(cell[0])-ord('a')+1, ord(cell[1])-ord('0'))
        cell = (cell[0]*2 - 1, cell[1]*2-1)
        return cell
    
    def get_path_from_cell_to_gutter(self,cell):
        source = self.get_coordinates_from_uci(cell)
        sink = self.get_gutter_position(cell)
        return self.get_path_source_sink(source,sink,False)

    def get_gutter_position(self,cell):
        position = self.get_coordinates_from_uci(cell)
        return min([(0,position[1]),(16,position[1]),(position[0],0),(position[0],16)], key=lambda x:abs((x[0]-position[0])**2 + (x[1]-position[1])**2))
        
