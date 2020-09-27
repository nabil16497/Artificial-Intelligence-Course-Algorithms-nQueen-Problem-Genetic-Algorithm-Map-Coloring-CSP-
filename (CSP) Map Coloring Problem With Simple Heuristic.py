
def start():
    maxcolor=3
    firstnode=''
    neighbourNumber = 0
    for node, neighbours in adjacencyList.items():
            if (len(neighbours) > neighbourNumber and color[node] == 0):
                neighbourNumber = len(neighbours)
                firstnode = node
    if possibleColor(firstnode, maxcolor):
        return True
    else:
        print("Can't color the map with only 3 colors.")
        return False


def possibleColor(node, maxcolor):
    
    if node == '':
        for key, value in color.items():
            if value == 0:
                possibleColor(key, maxcolor)
        return True

    for c in range(1, maxcolor+1):
        if canColor(node, c):
            color[node] = c
            shift=''
            if possibleColor(shift, maxcolor):
                return True
            else:
                color[node] = 0

    return False


def canColor(node, c):
    return all([color[neighbours] != c for neighbours in adjacencyList[node]])


    
def colorName(color):
    if(color==1): return 'RED'
    elif(color==2): return 'GREEN'
    elif(color==3): return 'BLUE'



adjacencyList = {
    'WA': ['NT', 'SA'],
    'Q': ['NT', 'SA', 'NSW'],
    'T': [],
    'V': ['SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NT': ['WA', 'SA', 'Q'],
    'NSW': ['SA', 'Q', 'V'],
    
    
};

color = {
    'WA': 0,
    'Q': 0,
    'T': 0,
    'V': 0,
    'SA': 0,
    'NT': 0,
    'NSW': 0
};
start()

for node, color in color.items():
    print(node,':',colorName(color))
