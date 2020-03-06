from collections import deque,defaultdict
from sys import exit
class graph():

    def __init__(self,n,e):
        self.v_dict = defaultdict(list)
        self.edgelist = e
        self.node_list = n
        self.visited = ''

    def printGraph(self):
        print("Adjacency List: ",self.v_dict,'\n\n',"Edge list: ",self.edgelist)

    def adj_v(self):

        for a,b in self.edgelist:
            self.v_dict[a].append(b)
            self.v_dict[b].append(a)    #Comment this line for directed graphs
        
        print(self.v_dict)


    def bfs(self,source):
        queue = deque()
        queue.append(source)
        self.visited += source
        print('BFS\n')
        print("Visited: {}".format(self.visited))
        while(len(queue)!=0):
            print(queue)
            u = queue.popleft()
            for v in self.v_dict[u]:
                if v not in self.visited:
                    queue.append(v)
                    self.visited += v
            print("Visited: {}".format(self.visited))

def createGraphBfs(n,e):

    G = graph(n,e)
    G.adj_v()
    #G.printGraph()
    G.bfs(str(input("Enter Source Node: ")))

def main():
    try:                                        #if input file is not present then it is created
        input_file = open("input.txt","r+")
    except:
        print("Creating input file....")
        input_file = open("input.txt","w+")
    if(input_file.readline() == ''):
        print("Write to file then execute ... exiting program")
        exit()
    input_file.seek(0,0)#set pointer to beginning of file
    v_n = input_file.readline().strip().split(' ')
    e_n = input_file.readline().strip().split(' ')
    input_file.close()
    y_n = []
    for e in e_n:
        y_n.append(tuple(e))
    print(v_n,y_n)
    createGraphBfs(v_n,y_n)

main()
# If input file is not created .... then output will be :- 
# Creating input file....
# Write to file then execute ... exiting program
#(run the script again and search will execute)#
############################

# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] # Nodelist
# [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G'), ('E', 'H'), ('H', 'I'), ('H', 'J')] #edgelist
#Adjacency List# {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F', 'G'], 'D': ['B'], 'E': ['B', 'H'], 'F': ['C'], 'G': ['C'], 'H': ['E', 'I', 'J'], 'I': ['H'], 'J': ['H']})
# Enter Source Node: A
# BFS

# Visited: A
# deque(['A'])
# Visited: ABC
# deque(['B', 'C'])
# Visited: ABCDE
# deque(['C', 'D', 'E'])
# Visited: ABCDEFG
# deque(['D', 'E', 'F', 'G'])
# Visited: ABCDEFG
# deque(['E', 'F', 'G'])
# Visited: ABCDEFGH
# deque(['F', 'G', 'H'])
# Visited: ABCDEFGH
# deque(['G', 'H'])
# Visited: ABCDEFGH
# deque(['H'])
# Visited: ABCDEFGHIJ
# deque(['I', 'J'])
# Visited: ABCDEFGHIJ
# deque(['J'])
# Visited: ABCDEFGHIJ