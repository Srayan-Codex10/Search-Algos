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
        self.edgelist.append(tuple(input().split(' ')))

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
# 
# Enter number of nodes: 
# 15
# Enter number of edges
# 14
# Enter nodes
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14 
# 15
# Enter edges
# enter the node-pairs for edge
# 1 2
# enter the node-pairs for edge
# 1 3
# enter the node-pairs for edge
# 1 4
# enter the node-pairs for edge
# 2 5
# enter the node-pairs for edge
# 2 6
# enter the node-pairs for edge
# 2 7
# enter the node-pairs for edge
# 3 8
# enter the node-pairs for edge
# 8 9
# enter the node-pairs for edge
# 8 10
# enter the node-pairs for edge
# 4 11
# enter the node-pairs for edge
# 11 12
# enter the node-pairs for edge
# 12 13
# enter the node-pairs for edge
# 12 14
# enter the node-pairs for edge
# 12 15
# {'1': ['2', '3', '4'], '2': ['1', '5', '6', '7'], '3': ['1', '8'], '4': ['1', '11'], '5': ['2'], '6': ['2'], '7': ['2'], '8': ['3', '9', '10'], '9': ['8'], 
# '10': ['8'], '11': ['4', '12'], '12': ['11', '13', '14', '15'], '13': ['12'], '14': ['12'], '15': ['12']}
#  [('1', '2'), ('1', '3'), ('1', '4'), ('2', '5'), ('2', '6'), ('2', '7'), ('3', '8'), ('8', '9'), ('8', '10'), ('4', '11'), ('11', '12'), ('12', '13'), ('12', '14'), ('12', '15')]
# Enter Source Node: 1
# BFS

# deque(['1'])
# Visited ['1']
# deque(['2', '3', '4'])
# Visited ['1', '2']
# deque(['3', '4', '5', '6', '7'])
# Visited ['1', '2', '3']
# deque(['4', '5', '6', '7', '8'])
# Visited ['1', '2', '3', '4']
# deque(['5', '6', '7', '8', '11'])
# Visited ['1', '2', '3', '4', '5']
# deque(['6', '7', '8', '11'])
# Visited ['1', '2', '3', '4', '5', '6']
# deque(['7', '8', '11'])
# Visited ['1', '2', '3', '4', '5', '6', '7']
# deque(['8', '11'])
# Visited ['1', '2', '3', '4', '5', '6', '7', '8']
# deque(['11', '9', '10'])
# Visited ['1', '2', '3', '4', '5', '6', '7', '8', '11']
# deque(['9', '10', '12'])
# Visited ['1', '2', '3', '4', '5', '6', '7', '8', '11', '9']
# deque(['10', '12'])
# Visited ['1', '2', '3', '4', '5', '6', '7', '8', '11', '9', '10']
# deque(['12'])
# Visited ['1', '2', '3', '4', '5', '6', '7', '8', '11', '9', '10', '12']
# deque(['13', '14', '15'])
# Visited ['1', '2', '3', '4', '5', '6', '7', '8', '11', '9', '10', '12', '13']
# deque(['14', '15'])
# Visited ['1', '2', '3', '4', '5', '6', '7', '8', '11', '9', '10', '12', '13', '14']
# deque(['15'])
# Visited ['1', '2', '3', '4', '5', '6', '7', '8', '11', '9', '10', '12', '13', '14', '15']
#  