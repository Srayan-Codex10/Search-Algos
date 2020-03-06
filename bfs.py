# class node:
#     pass
from collections import deque
from sys import exit
class graph():

    def __init__(self,n,e):
        self.v_dict = {}
        self.edgelist = e
        self.node_list = n
        self.visited = []

    def printGraph(self):
        print("Adjacency List: ",self.v_dict,'\n\n',"Edge list: ",self.edgelist)

    def adj_v(self):
        for node in self.node_list:
            self.v_dict[node] = []

        for key in self.v_dict:
            for e_tup in self.edgelist:
                if key in e_tup:
                    self.v_dict[key].append(e_tup[0])   #In case of directed graph comment this line
                    self.v_dict[key].append(e_tup[1])

        for key in self.v_dict: #In case of directed graph comment out the loop
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

def createGraphBfs(n,e):

    G = graph(n,e)
    G.adj_v()
    G.printGraph()
    G.bfs(str(input("Enter Source Node: ")))

def main():
    #if input file is not present then it is created
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
    #print(v_n,y_n)
    createGraphBfs(v_n,y_n)

main()
# If input file is not created .... then output will be :- 
# Creating input file....
# Write to file then execute ... exiting program
#(run the script again and search will execute)#
############################

# Adjacency List:  {'A': ['B', 'G', 'H', 'E'], 'B': ['A', 'D', 'C', 'G', 'H'], 'C': ['D', 'B', 'H', 'E'], 'D': ['C', 'B'], 'E': ['F', 'A', 'C'], 'F': ['G', 'E'], 'G': ['A', 'B', 'F'], 'H': ['A', 'B', 'C']}

#  Edge list:  [('A', 'B'), ('C', 'D'), ('B', 'D'), ('B', 'C'), ('A', 'G'), ('B', 'G'), ('F', 'G'), ('A', 'H'), ('B', 'H'), ('C', 'H'), ('E', 'F'), ('E', 'A'), ('E', 'C')]
# Enter Source Node: A
# BFS

# deque(['A'])
# Visited ['A']
# deque(['B', 'G', 'H', 'E'])
# Visited ['A', 'B']
# deque(['G', 'H', 'E', 'D', 'C'])
# Visited ['A', 'B', 'G']
# deque(['H', 'E', 'D', 'C', 'F'])
# Visited ['A', 'B', 'G', 'H']
# deque(['E', 'D', 'C', 'F'])
# Visited ['A', 'B', 'G', 'H', 'E']
# deque(['D', 'C', 'F'])
# Visited ['A', 'B', 'G', 'H', 'E', 'D']
# deque(['C', 'F'])
# Visited ['A', 'B', 'G', 'H', 'E', 'D', 'C']
# deque(['F'])
# Visited ['A', 'B', 'G', 'H', 'E', 'D', 'C', 'F']