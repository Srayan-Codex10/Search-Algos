# class node:
#     pass
from collections import deque
class graph():

    def __init__(self,n,e):
        self.no_v = n
        self.no_e = e
        self.v_dict = {}
        self.edgelist = []
        self.visited = []

    def add_nodes(self,node):

        self.v_dict[node] = []
    
    def add_edge(self):
        print("enter the node-pairs for edge")
        self.edgelist.append(tuple(input()))

    def printGraph(self):
        print(self.v_dict,'\n',self.edgelist)

    def adj_v(self):

        for key in self.v_dict:
            for e_tup in self.edgelist:
                if key in e_tup:
                    self.v_dict[key].append(e_tup[0])
                    self.v_dict[key].append(e_tup[1])
        #print(self.v_dict)
        for key in self.v_dict:
             while key in self.v_dict[key]:
                 self.v_dict[key].remove(key)

        #print(self.v_dict)

    def bfs(self,source):
       queue = deque()
       queue.append(source)
       print('BFS\n')
       while(len(queue)!=0):
           print(queue)
           x = queue.popleft()
           self.visited.append(x)
           print("Visited",self.visited)
           for i in range(0,len(self.v_dict[x])):
               if((self.v_dict[x][i] not in self.visited) & (self.v_dict[x][i] not in queue)):
                   queue.append(self.v_dict[x][i])

def createGraphBfs():
    print("Enter number of nodes: ")
    n_nodes = int(input())
    print("Enter number of edges")
    n_edges = int(input())

    G = graph(n_nodes,n_edges)

    print("Enter nodes")
    for i in range(0,n_nodes):
        G.add_nodes(str(input()))

    print("Enter edges")
    for i in range(0,n_edges):
        G.add_edge()
    
    G.adj_v()
    G.printGraph()
    G.bfs(str(input("Enter Source Node: ")))


def main():
    createGraphBfs()

main()
# SAMPLE INPUT & OUTPUT 
# Enter number of nodes: 
# 15
# Enter number of edges
# 14
# Enter nodes
# A
# B
# C
# D
# E
# F
# G
# H
# I
# J
# K
# L
# M
# N
# O
# Enter edges
# enter the node-pairs for edge
# AB
# enter the node-pairs for edge
# AC
# enter the node-pairs for edge
# AD
# enter the node-pairs for edge
# BE
# enter the node-pairs for edge
# BF
# enter the node-pairs for edge
# BG
# enter the node-pairs for edge
# CJ
# enter the node-pairs for edge
# JK
# enter the node-pairs for edge
# JL
# enter the node-pairs for edge
# DM
# enter the node-pairs for edge
# MN
# enter the node-pairs for edge
# NH
# enter the node-pairs for edge
# NI
# enter the node-pairs for edge
# NO
# {'A': ['B', 'C', 'D'], 'B': ['A', 'E', 'F', 'G'], 'C': ['A', 'J'], 'D': ['A', 'M'], 'E': ['B'], 'F': ['B'], 'G': ['B'], 'H': ['N'], 'I': ['N'], 'J': ['C', 'K', 'L'], 'K': ['J'], 'L': ['J'], 'M': ['D', 'N'], 'N': ['M', 'H', 'I', 'O'], 'O': ['N']}
#  [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('B', 'F'), ('B', 'G'), ('C', 'J'), ('J', 'K'), ('J', 'L'), ('D', 'M'), ('M', 'N'), ('N', 'H'), ('N', 'I'), ('N', 'O')]
# Enter Source Node: A
# BFS

# deque(['A'])
# Visited ['A']
# deque(['B', 'C', 'D'])
# Visited ['A', 'B']
# deque(['C', 'D', 'E', 'F', 'G'])
# Visited ['A', 'B', 'C']
# deque(['D', 'E', 'F', 'G', 'J'])
# Visited ['A', 'B', 'C', 'D']
# deque(['E', 'F', 'G', 'J', 'M'])
# Visited ['A', 'B', 'C', 'D', 'E']
# deque(['F', 'G', 'J', 'M'])
# Visited ['A', 'B', 'C', 'D', 'E', 'F']
# deque(['G', 'J', 'M'])
# Visited ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# deque(['J', 'M'])
# Visited ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'J']
# deque(['M', 'K', 'L'])
# Visited ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'J', 'M']
# deque(['K', 'L', 'N'])
# Visited ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'J', 'M', 'K']
# deque(['L', 'N'])
# Visited ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'J', 'M', 'K', 'L']
# deque(['N'])
# Visited ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'J', 'M', 'K', 'L', 'N']
# deque(['H', 'I', 'O'])
# Visited ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'J', 'M', 'K', 'L', 'N', 'H']
# deque(['I', 'O'])
# Visited ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'J', 'M', 'K', 'L', 'N', 'H', 'I']
# deque(['O'])
# Visited ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'J', 'M', 'K', 'L', 'N', 'H', 'I', 'O']