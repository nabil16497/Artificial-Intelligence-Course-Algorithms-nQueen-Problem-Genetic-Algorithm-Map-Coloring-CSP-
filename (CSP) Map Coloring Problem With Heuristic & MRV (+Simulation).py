def countNeighboursandColors():
    
    for state in list(Graph.keys()):
        Adjacency.append([state, len(Graph[state]),len(ColorDomain[state])])
    print("Node, Number of Neighbours, Initially Available Number of Colors")
    print("_________________________________________________________________")
    print(Adjacency)
    print("_________________________________________________________________")
    print()
def sort():
    Adjacency.sort(key = lambda x: x[1],reverse=True)
    print("Sorted According to Number of Neighbours-")
    print(Adjacency)
    print("_________________________________________________________________")
    print()

def removeColors():
    print("New Color Choice List For Neighbours-")
    print("_________________________________________________________________")
    print()
    print(state, " : ",end="")
    AssignedColor[state] = ColorDomain[state][0]
    for m in Graph[state]:
        if (AssignedColor[state] in ColorDomain[m]):
            ColorDomain[m].remove(AssignedColor[state])
        print(m,ColorDomain[m],end="")
    print()        
    print("_________________________________________________________________")
    print()
    
    
def sortColorwise():
    for s in Adjacency:
        s[2]=len(ColorDomain[s[0]])
    Adjacency.sort(key = lambda x: x[2],reverse=False)
    print("Available-")
    print("Node, Number of Neighbours, Initially Available Number of Colors")
    print("_________________________________________________________________")
    print(Adjacency)
    print("_________________________________________________________________")
    print()
    
    
Graph = {'SA': ['WA', 'NT', 'Q', 'NSW', 'V'], 
         'Q': ['SA', 'NT', 'NSW'],
         'NT': ['Q', 'WA', 'SA'],
         'NSW': ['Q', 'V', 'SA'],
         'WA': ['SA', 'NT'],
         'V': ['SA', 'NSW'],  
         'T': []}



ColorDomain = {'SA': ['red', 'green', 'blue'], 
               'Q': ['red', 'green', 'blue'], 
               'NT': ['red', 'green', 'blue'], 
               'NSW': ['red', 'green', 'blue'], 
               'WA': ['red', 'green', 'blue'], 
               'V': ['red', 'green', 'blue'], 
               'T': ['red', 'green', 'blue']}

AssignedColor = {}
Adjacency = []


countNeighboursandColors()
sort()


while Adjacency:
    state=Adjacency[0][0]
    Adjacency.pop(0)
    removeColors()
    sortColorwise()

print()    
print("After Colored")
print(AssignedColor)
