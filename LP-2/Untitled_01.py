# #BFS Algorithm

    #     A
    #   /   \
    #  B     C
    #   \   /
    #     D
    #   /   \
    #  E     F
    
graph = {
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D'],
    'D':['B','C','E','F'],
    'E':['D'],
    'F':['D']
}

visited = []
queue = []
def bfs(graph,root,end):
    queue.append(root)
    
    while queue:
        m = queue.pop(0)
        if m not in visited:
            visited.append(m)
        
        if m == end:
            print("The travesal is = ")
            for i in visited:
                print(i)
            print("node is found !")
            break
        else :
            for n in graph[m]:
                if n not in visited:
                    queue.append(n) 
                    
    if end not in visited:
        print("Node not found !")
    
bfs(graph,'A','B')

# DFS____________________________________________________________________________

    #     A
    #   /   \
    # B       C
    #   \   /
    #     D
    #   /   \
    #  E     F
    

visited = []
stack = []

def dfs(graph, start, goal):
    print("DFS traveral is: ")
    stack.append(start)
    while stack:
        
        node = stack.pop(-1)
        
        if node not in visited:
            visited.append(node)
        
        print("Node: ", node)
        if node == goal:
            print("Goal node found!")
            return
        for n in graph[node]:
            if n not in visited:
                stack.append(n)

dfs(graph, 'A', "D")





