import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

N=17

def remove_connecting_edges(G):
    for x in range(1, N, 2):
        for y in range(1, N, 2):
            for i in range(-1, 2):
                for j in range (-1, 2):
                    u = (x, y)
                    v = (x+i, y+j)
                    if(x+i >=0 and y+j >=0 and G.has_edge(u, v)):
                        G.remove_edge(u, v)


def add_connecting_edges(G, u):
    for i in range(-1, 2):
        for j in range(-1, 2):
            x = u[0]
            y = u[1]
            v= (x+i, y+j)
            if(x+i>=0 and y+j >=0 and x+i < N and y+j < N and u != v and ((x+i == x) or (y+j == y))):
                G.add_edge(u, v)


def get_coordinates_from_move(move):
    source = (ord(move[0])-ord('a')+1, ord(move[1])-ord('0'))
    source = (source[0]*2 - 1, source[1]*2-1)
    sink = (ord(move[2])-ord('a')+1, ord(move[3])-ord('0'))
    sink = (sink[0]*2 - 1, sink[1]*2-1)
    return (source, sink)


def convert_path_arduino(path):
    moves = []
    for (source, sink) in path:
        x_source = source[0]
        y_source = source[1]
        x_sink = sink[0]
        y_sink = sink[1]
        move = (x_source > x_sink) * 1 + (x_source < x_sink) * 2 + (y_source > y_sink) * 3 + (y_source < y_sink) * 4
        moves.append(move)
    return moves


def get_path(move):
    G=nx.grid_2d_graph(N, N)

    (source, sink) = get_coordinates_from_move(move)
    
    H = G.copy()

    remove_connecting_edges(H)
    add_connecting_edges(H, source)
    add_connecting_edges(H, sink)

    path = nx.shortest_path(H,source=source, target=sink, method='dijkstra')
    path_edges = list(zip(path,path[1:]))
    moves = convert_path_arduino(path_edges)
    return moves