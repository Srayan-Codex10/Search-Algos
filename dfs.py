from time import sleep
class node():
    #pass
    name = ''
    color = ''
    pi = ''
    dis_time = 0 
    finish_time = 0

    def __init__(self):
        self.color = 'white'

time = 0
edge_list = []
node_list = []
adj_list = {}

def createGraph():
    i = 0
    print("Enter number of nodes in graph")
    n = int(input("Nodes: "))

    print("Enter number of edges in graph")
    e = int(input("Edges: "))

    print("Enter node names")
    while(i<n):
        g = node()
        g.name = str(input('Node: '))
        adj_list[g.name] = []
        node_list.append(g)
        print(g.color)
        i += 1
    
    i = 0
    print("Enter node pairs for edge")
    while(i<e):
        edge_list.append(tuple(input("Edge: ").split(' ')))
        i += 1

    print("Creating adjacency list....")
    sleep(0.99)
    for key in adj_list:
        for e_tup in edge_list:
            if key in e_tup:
                adj_list[key].append(e_tup[0])
                adj_list[key].append(e_tup[1])

    for key in adj_list:
        while key in adj_list[key]:
            adj_list[key].remove(key)


def dfs(G):
    pass
def dfs_visit(G,u):
    pass

createGraph()

# print(adj_list)
# print(edge_list)
# for vertex in node_list:
#     print(vertex.name,vertex.color,vertex.pi,vertex.time,vertex.dis_time,vertex.finish_time)