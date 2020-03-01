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
