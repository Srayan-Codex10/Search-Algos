from sys import exit
from collections import defaultdict
class node():
    name = ''
    color = ''
    pi = ''
    dis_time = 0 
    finish_time = 0

    def __init__(self,name):
        self.name = name
        self.color = 'white'

time = 0
edge_list = []
node_list = []
adj_list = defaultdict(list)

def createGraph(n,e):
    
    for name in n:
        node_list.append(node(name))
    
    global edge_list
    edge_list = e

    for a,b in edge_list:
        adj_list[a].append(b)
        adj_list[b].append(a)

    #print('Edges: ',edge_list,'\n\n','Adjacency List: ',adj_list)


def dfs():
    for vertex in node_list:
        if vertex.color == 'white':
            dfs_visit(vertex)

def dfs_visit(u):
    u.color = 'gray'
    print("Visited: ",u.name,'\t',"Predecessor: ",u.pi)
    global time 
    time += 1
    u.dis_time = time
    for v in adj_list[u.name]:
        for n in node_list:
            if n.name == v:
                if n.color == 'white':
                    n.pi = u.name
                    dfs_visit(n)

    u.color = 'black'
    time += 1
    u.finish_time = time

def main():
    try:
        input_file = open("input.txt","r+")
    except:
        print("Creating input file....")
        input_file = open("input.txt","w+")
    if(input_file.readline() == ''):
        print("Write to file then execute ... exiting program")
        exit()
    l = 0
    input_file.seek(0,0)#set pointer to beginning of file
    while l < 2:
        if l == 1:
            e_n = input_file.readline().strip().split(' ')
        else:
            v_n = input_file.readline().strip().split(' ')
        l += 1
    input_file.close()
    y_n = []
    for e in e_n:
        y_n.append(tuple(e))
    createGraph(v_n,y_n)
    dfs()


main()

print("Node",'\t','Discovery Time','\t','Finish Time','\t','Predecessor','\t','Color')
for vertex in node_list:
    print(vertex.name,'\t',vertex.dis_time,'\t\t\t',vertex.finish_time,'\t\t',vertex.pi,'\t\t',vertex.color)

# Visited:  A      Predecessor:
# Visited:  B      Predecessor:  A
# Visited:  D      Predecessor:  B
# Visited:  E      Predecessor:  B
# Visited:  H      Predecessor:  E
# Visited:  I      Predecessor:  H
# Visited:  J      Predecessor:  H
# Visited:  C      Predecessor:  A
# Visited:  F      Predecessor:  C
# Visited:  G      Predecessor:  C
# Node     Discovery Time          Finish Time     Predecessor     Color
# A        1                       20                              black
# B        2                       13              A               black
# C        14                      19              A               black
# D        3                       4               B               black
# E        5                       12              B               black
# F        15                      16              C               black
# G        17                      18              C               black
# H        6                       11              E               black
# I        7                       8               H               black
# J        9                       10              H               black
