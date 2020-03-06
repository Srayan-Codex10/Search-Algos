from time import sleep
from sys import exit
class node():
    #pass
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
adj_list = {}

def createGraph(n,e):

    for vertex in n:
        node_list.append(node(vertex))
    
    for n_object in node_list:
        adj_list[n_object.name] = []

    edge_list = e

    for key in adj_list:
        for e_tup in edge_list:
            if key in e_tup:
                adj_list[key].append(e_tup[0])
                adj_list[key].append(e_tup[1])

    for key in adj_list:
        while key in adj_list[key]:
            adj_list[key].remove(key)
            
    print(edge_list,'\n\n',node_list,'\n\n',adj_list)


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

main()

def dfs():
    for vertex in node_list:
        if vertex.color == 'white':
            dfs_visit(vertex)

def dfs_visit(u):
    print(u,u.name)
    u.color = 'gray'
    global time 
    time += 1
    u.dis_time = time
    # for v in adj_list[u.name]:
    #     for n in node_list:
    #         if n.name == v:
    #             n.pi = v
    #             dfs_visit(n)

    u.color = 'black'
    time += 1
    u.finish_time = time